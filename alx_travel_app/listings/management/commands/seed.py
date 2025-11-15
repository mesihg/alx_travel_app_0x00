from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the listing table with sample listings"

    def handle(self, *args, **kwargs):
        titles = [
            'Downtown Apartment', 'Cozy Cabin', 'Luxury Villa',
            'Beachside Bungalow', 'Mountain Retreat'
        ]
        locations = ['Mombasa', 'Nairobi',
                     'Kigali', 'Cape Town', 'Addis Ababa']
        for _ in range(10):
            listing = Listing.objects.create(
                title=random.choice(titles),
                description="A good place to stay!!",
                location=random.choice(locations),
                price_per_night=random.uniform(200.0, 1000.0)
            )
            self.stdout.write(self.style.SUCCESS(f'Created: {listing}'))
