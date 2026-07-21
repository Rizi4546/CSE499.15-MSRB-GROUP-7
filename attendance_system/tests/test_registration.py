from database.db_manager import init_database, get_all_students
from utils.registration import register_student

def run_tests():
    # Initialize DB
    init_database()
    
    # Register 5 test subjects
    test_students = [
        ("2228974", "Prio"),
        ("2314145", "Adnan"),
        ("2413412", "Rizvi"),
        ("2134235", "Shamsi"),
        ("2431345", "Ahsan")
    ]
    
    for sid, name in test_students:
        register_student(sid, name, num_samples=10)
    
    # Verify storage
    students = get_all_students()
    print(f"\n{'='*50}")
    print(f"Total students in database: {len(students)}")
    for s in students:
        print(f"  - {s['student_id']}: {s['name']} (embedding dim: {len(s['embedding'])})")
    
    assert len(students) == 5, "Expected 5 students"
    assert len(students[0]['embedding']) == 128, "Expected 128-d embedding"
    print("\n✓ All tests passed!")

if __name__ == "__main__":
    run_tests()