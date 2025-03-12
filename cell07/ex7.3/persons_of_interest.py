from datetime import datetime

def famous_births(people):
    """
    รับพจนานุกรมของบุคคลในประวัติศาสตร์และเรียงลำดับตามวันเกิด
    :param people: พจนานุกรมที่มีข้อมูลของบุคคล โดยแต่ละรายการประกอบด้วย 'name' และ 'date_of_birth'
    :return: ไม่มีค่าผลลัพธ์ แต่จะแสดงข้อมูลของบุคคลเรียงตามวันเกิด
    """
    for person in people:
        person['date_of_birth'] = datetime.strptime(person['date_of_birth'], '%Y-%m-%d')
    
    people_sorted = sorted(people, key=lambda x: x['date_of_birth'])

    for person in people_sorted:
        print(f"{person['name']} - {person['date_of_birth'].strftime('%B %d, %Y')}")

if __name__ == "__main__":
    famous_people = [
        {'name': 'Albert Einstein', 'date_of_birth': '1879-03-14'},
        {'name': 'Marie Curie', 'date_of_birth': '1867-11-07'},
        {'name': 'Isaac Newton', 'date_of_birth': '1643-01-04'},
        {'name': 'Galileo Galilei', 'date_of_birth': '1564-02-15'}
    ]
    
    famous_births(famous_people)
