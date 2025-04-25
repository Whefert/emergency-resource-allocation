from Controller.StatusController import create_status, get_all_statuses
from unittest import TestCase
from Model.Status import Status

class TestStatusController(TestCase):
    def setUp(self):
        # This method will run before each test
        self.status = Status(name="Test Status", description="Test Description")
        self.status_id = create_status(self.status)

    def tearDown(self):
        # This method will run after each test
        pass  # You can add code to clean up the database if needed

    def test_create_status(self):
        # Test creating a status
        self.assertIsNotNone(self.status_id, "Status ID should not be None after creation")

    def test_get_all_statuses(self):
        # Test getting all statuses
        statuses = get_all_statuses()
        self.assertIsInstance(statuses, list, "Statuses should be returned as a list")
        self.assertGreater(len(statuses), 0, "There should be at least one status in the database")

