#!/usr/bin/env python

import argparse

def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('filename',type=str,help='write to filename')
    parser.add_argument('size',type=int,help='how many commands to create')
    return parser.parse_args()


def createCommandFile(filename,size:int):
    # Build 100 SEND commands
    send_cmds = [f"SEND doc{i}" for i in range(size)]
    # Interleave PRINT commands for first 50
    commands = []
    for i in range(size//2):
        commands.append(send_cmds[i])
        commands.append("PRINT")
    # Add the rest without printing yet
    commands.extend(send_cmds[size//2:])
    # Peek at the next item, then drain them all
    commands.append("NEXT")
    commands.extend(["PRINT"] * (size//2 + 10))  # 50 left + 10 extra empties
    
    with open(filename, 'w') as f:
        f.writelines(item + "\n" for item in commands)
    

def main():
    args=parse_args()

    createCommandFile(args.filename,args.size)



if __name__ == '__main__':
    main()