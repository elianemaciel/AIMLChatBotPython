import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("start.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    question = input("Enter your message >> ")
    print(kernel.respond(question))

