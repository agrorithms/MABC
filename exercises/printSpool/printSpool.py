class PrintSpooler:
    def __init__(self):
        self.size=0
        self.queue=[]
    
    def add_document(self,name:str):
        self.queue.append(name)
        self.size+=1

    def print_next(self):
        if self.queue==[]:
            return None
        self.size-=1
        return self.queue.pop(0)
    
    def peek(self):
        if self.queue==[]:
            return None
        return self.queue[0]

    def __len__(self):
        return self.size


def simulate(commands: list[str])-> list[str]:
    printspool = PrintSpooler()
    output = []
    for cmd in commands:
        if cmd == 'PRINT':
            step=printspool.print_next()
            if step == None:
                step = 'No documents waiting'
            else:
                step = 'Printing ' + step
            output.append(step)
            print(step)
            

        elif cmd == 'NEXT':
            step=printspool.peek()
            if step == None:
                step = 'Queue empty'
            else: 
                step = 'Next is ' + step
            output.append(step)
            print(step)
        elif cmd[:4]=='SEND':
            printspool.add_document(cmd[5:])
        else:
            return ['Invalid command: ' + cmd]
    return output