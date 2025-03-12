def average(grades):
    """
    คำนวณค่าเฉลี่ยของคะแนนการบ้านจากพจนานุกรมที่เชื่อมโยงชื่อจริงของนักเรียนกับคะแนน
    :param grades: พจนานุกรมที่มีชื่อของนักเรียนเป็นคีย์ และคะแนนการบ้านเป็นค่า
    :return: ค่าเฉลี่ยของคะแนน
    """

    if not grades:
        return 0
    
    total_score = sum(grades.values())
    
    avg = total_score / len(grades)
    
    return avg

if __name__ == "__main__":
    student_grades = {
        'John': 69,
        'Alice': 56,
        'Bob': 52,
        'Eva': 49,
    }
    
    class_average = average(student_grades)
    
    print(f'ค่าเฉลี่ยของการบ้านคือ: {class_average}')
