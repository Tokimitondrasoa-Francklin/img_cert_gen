import cv2


list_of_names = []

def cleanup_data():
    with open("name-list-data.txt") as file:
        for line in file:
            list_of_names.append(line.strip())
            
def generate_certificate():
    for name in list_of_names:
        template = cv2.imread("certificate-template.png")
        cv2.putText(template, name, (170, 315), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 25, 250), 1, cv2.LINE_AA)
        cv2.imwrite(f'genereated-certificates/{name}.png',template )
            
cleanup_data()
generate_certificate()