from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Listing(models.Model):
    """Represents a travel listing."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_length=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """Represents a booking made for a listing by a user."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookings')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.listing.title}"


class Review(models.Model):
    """Represents reviews made for a listing by a user."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.listing.title} by {self.user.username}"
