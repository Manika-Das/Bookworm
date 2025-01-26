from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q

def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')

def home(request):
    """
    Display a list of books with optional search functionality.
    Users can search by book name, author name, or genre.
    """
    books = Book.objects.all()
    query = request.GET.get('search', '')

    if query:
        books = books.filter(
            Q(book_name__icontains=query) |
            Q(author_name__icontains=query) |
            Q(genre__icontains=query)
        )
    
    return render(request, 'home.html', {'books': books, 'query': query})

def login(request):
    """
    Render the login page.
    """
    return render(request, 'login.html')

def register(request):
    """
    Render the registration page.
    """
    return render(request, 'regi_login.html')

def otp_verification(request):
    """
    Render the OTP verification page.
    """
    return render(request, 'OTP.html')

def readnow(request, book_id):
    """
    Display the details of a specific book for reading.
    """
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'readnow.html', {'book': book})

def contribution(request):
    """
    Allow users to contribute by adding new books.
    Handles form submissions via POST requests.
    """
    if request.method == 'POST':
        try:
            # Retrieve form data
            book_name = request.POST.get('book_name')
            author_name = request.POST.get('author_name')
            genre = request.POST.get('genre')
            thumbnail_url = request.POST.get('thumbnail_url')
            ratings = request.POST.get('ratings')
            pdf_link = request.POST.get('pdf_link')
            language = request.POST.get('language')
            isbn_number = request.POST.get('isbn_number')
            publishing_date = request.POST.get('publishing_date')
            book_pages = request.POST.get('book_pages')

            # Validate required fields
            if not all([book_name, author_name, genre, pdf_link, language]):
                return render(request, 'contribution.html', {'error': "All required fields must be filled."})

            # Save the book to the database
            Book.objects.create(
                book_name=book_name,
                author_name=author_name,
                genre=genre,
                thumbnail_url=thumbnail_url,
                ratings=ratings,
                pdf_link=pdf_link,
                language=language,
                isbn_number=isbn_number,
                publishing_date=publishing_date,
                book_pages=book_pages
            )
            return render(request, 'contribution.html', {'success': True})

        except Exception as e:
            return render(request, 'contribution.html', {'error': f"An error occurred: {str(e)}"})

    return render(request, 'contribution.html')

def page_turner(request, book_id):
    """
    Allow users to view a book page by page.
    """
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'pageturner.html', {'book': book})

def book_preview(request):
    """
    Render the book preview page.
    """
    return render(request, 'bookpreview.html')

def my_shelf(request):
    """
    Render the 'My Shelf' page, showing the user's saved books.
    """
    # Optionally, you can filter books associated with the logged-in user.
    # Example:
    # user_books = Book.objects.filter(user=request.user)
    return render(request, 'myshelf.html')

def faq(request):
    """
    Render the FAQ page.
    """
    return render(request, 'faq.html')
