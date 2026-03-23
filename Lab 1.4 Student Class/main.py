from student import Student

def main():
    stu = Student("Job Bluthe", 42, ["English Composition", "College Algebra"])
    print(f"Starting student: {stu}")
    
    # add some classes
    print(f"\nAdd class Psychology I: {stu.addClass('Psychology I')} [should be True]")
    print(f"Add class American History: {stu.addClass('American History')} [should be True]")
    print(f"Add class English Composition: {stu.addClass('English Composition')} [should be False]")

    print(f"\nCurrent classes: {stu.getClasses()}")
    
    # remove some classes
    print(f"Remove class Psychology I: {stu.removeClass('Psychology I')} [should be True]")
    print(f"Remove class American History: {stu.removeClass('American History')} [should be True]")
    print(f"Remove class Underwater Basket Weaving: {stu.removeClass('Underwater Basket Weaving')} [should be False]")

    stu.setName("Bill Brasky")
    stu.setId(99)
    
    print(f"\nEnding student: {stu}")
    
if __name__ == "__main__":
    main()
