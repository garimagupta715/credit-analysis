from django.test import TestCase
from django.contrib.auth import get_user_model
##from django.contrib.auth.password_validation import password_changed

class ModelTests(TestCase):
    
    def test_creste_user_with_email(self):
        """Test creating a new user with email address"""
        email = 'test@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
            )
        
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    
    
    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'Test123')
        
        self.assertEqual(user.email, email.lower())
        
        

    def test_new_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
        
        
        
    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'test123'
            )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)