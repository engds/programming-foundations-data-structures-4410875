from collections import deque

printer_queue = deque()
printer_queue.append("Approval.pdf")
printer_queue.append("suspension.pdf")
printer_queue.append("meal plan.pdf")
 
while len(printer_queue)>0:
  document = printer_queue.popleft()
  #To remove the last item simply use pop
  print(f'Printing {document}')
