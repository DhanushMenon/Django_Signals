# myapp/views.py
from django.shortcuts import render
from .signals import emit_my_signal
import threading

# Function to handle Question 1 signal demonstration
def question_1_view(request):
    emit_my_signal()
    return render(request, 'myapp/question_1.html')

# Function to handle Question 2 signal threading demonstration
def question_2_view(request):
    output = []
    
    def emit_signal():
        output.append(f"Emitting signal thread: {threading.current_thread().name}")
        emit_my_signal()
    
    emit_signal()
    
    # Show output in the browser
    context = {'output': output}
    return render(request, 'myapp/question_2.html', context)

# If you had a 'test_signal' view, it might look like this:
def test_signal(request):
    emit_my_signal()
    return HttpResponse("Signal emitted")


# myapp/views.py
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Welcome to Django Signal Demo</h1>
        <a href='/question-1/'><button>Go to Question 1</button></a>
        <a href='/question-2/'><button>Go to Question 2</button></a>
        <a href='/test-signal/'><button>Test Signal</button></a>
        
        <a href='/question-3/'><button>Test Transaction Signal</button></a>
        <a href='/custom-classes/'><button>Custom Classes</button></a>
                        
    """)



# myapp/views.py
from django.http import HttpResponse
from .signals import emit_my_signal

# Test signal view
def test_signal(request):
    emit_my_signal()  # Emit the signal
    return HttpResponse("Signal sent successfully.")


from django.db import transaction
from django.http import HttpResponse
from .signals import my_signal

def question_3_view(request):
    # Emit signal within a database transaction
    with transaction.atomic():
        print("Before sending the signal in transaction")
        my_signal.send(sender=None)
        print("After sending the signal in transaction")

    return HttpResponse("Signal sent within a database transaction!")


# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

# Rectangle class definition
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# New view for custom classes
def custom_classes_view(request):
    rect = Rectangle(10, 5)

    # Prepare output for the template
    dimensions = list(rect)  # Convert the iterable to a list for rendering

    return render(request, 'myapp/custom_classes.html', {'dimensions': dimensions})
