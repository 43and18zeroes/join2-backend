# import json
# from kanban_app.models import Task

# data = [
#     {"category":"Technical Task","taskColumnOrder":1,"assignedTo":["victor@victor.de","dani@dani.de","lechner@lechner.de"],"title":"Implement Django Backend","firebaseId":"4bXhKJ8Eh2fyRHd13Uzn","subTasks":["Install Django","Install DRF"],"dueDate":"2024-11-29","subTasksCompleted":[False,False],"taskStatus":"todo","priority":"urgent","description":"With DRF"},
#     {"taskStatus":"done","priority":"urgent","category":"User Story","taskColumnOrder":1,"subTasks":[],"dueDate":"2024-09-06","description":"Secure and straightforward checkout process.","subTasksCompleted":[],"assignedTo":["lars.victor@email.com","wegner@wegner.de"],"title":"Customer journey","firebaseId":"dDnPCVYLgidAYLyF01LL"},
#     {"description":"Design and implement a responsive navigation menu that adapts to mobile and desktop views. Ensure that the menu is easy to use on touch devices and provides clear access to all major sections of the website.","assignedTo":["jan.fischer@email.com","kerstin.salzmann@email.com","sara.neumann@email.com","simon.frank@email.com"],"title":"Design a Mobile-Friendly Navigation Menu","subTasksCompleted":[True,True],"firebaseId":"qvo3G29NlzOngmhxzv37","priority":"medium","subTasks":["Navigation menu","Touch devices"],"dueDate":"2024-08-20","taskStatus":"awaitfeedback","category":"User Story","taskColumnOrder":1},
#     {"taskStatus":"inprogress","subTasks":["Mobil"],"taskColumnOrder":1,"dueDate":"2024-08-29","assignedTo":["bert@bert.de"],"title":"Test Cross-Browser Compatibility","subTasksCompleted":[False],"priority":"low","category":"Technical Task","description":"Check and correct any issues that arise in different web browsers (such as Chrome, Firefox, Safari, Edge).","firebaseId":"zrC1Glf3MQfYROitPxMY"}
# ]

# for task_data in data:
#     task = Task(**task_data)
#     task.save()
