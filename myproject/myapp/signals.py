# myapp/signals.py
import threading
from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler thread:", threading.current_thread().name)

# Emit the signal (this will be called manually elsewhere)
def emit_my_signal():
    print("Before sending the signal")
    print("Emitting signal thread:", threading.current_thread().name)
    my_signal.send(sender=None)
    print("After sending the signal")
