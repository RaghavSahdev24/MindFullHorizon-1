#!/usr/bin/env python3
"""
Script to add dummy users for testing.
"""

from app import app
from models import User, Gamification, db
from datetime import datetime

def add_dummy_users():
    with app.app_context():
        # Check if users already exist
        patient = User.query.filter_by(email='patient@example.com').first()
        provider = User.query.filter_by(email='provider@example.com').first()

        if patient:
            print("Patient user already exists")
        else:
            # Create patient user
            patient_user = User(
                email='patient@example.com',
                name='Demo Patient',
                role='patient',
                institution='Demo University'
            )
            patient_user.set_password('password')
            db.session.add(patient_user)
            db.session.flush()  # To get the ID

            # Create gamification profile
            gamification = Gamification(
                user_id=patient_user.id,
                points=0,
                streak=0,
                badges=[],
                last_activity=datetime.utcnow()
            )
            db.session.add(gamification)
            print("Patient user created")

        if provider:
            print("Provider user already exists")
        else:
            # Create provider user
            provider_user = User(
                email='provider@example.com',
                name='Demo Provider',
                role='provider',
                institution='Demo Hospital'
            )
            provider_user.set_password('password')
            db.session.add(provider_user)
            print("Provider user created")

        db.session.commit()
        print("Dummy users added successfully!")

if __name__ == '__main__':
    add_dummy_users()