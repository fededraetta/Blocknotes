#Block notes program
task = []
primo_task = input("Cosa devi fare oggi?\n")
task.append(primo_task)
i = "+"
while i == "+":
    a = input("Cos'altro devi fare? [\"stop\" to abort]\n")
    if a == "stop":
        i = "-"
    else:
        task.append(a)
        i = "+"
print("\n##############")
print("Agenda di oggi:")
print("##############\n")
for compiti in range(len(task)):
    print("·",task[compiti],"\n")

t = 1
while t == 1:
    premiperaggiungere = input("Premi \"+\" per aggiungere un task (\"close\" per chiudere, \"show\" per elenco)\n")
    if premiperaggiungere == "+":
        aggiungi = input("Cos'altro devi fare? (\"-\" per uscire)\n")
        if aggiungi == "-":
            break
        else:
            task.append(aggiungi)
        t = 1
    elif premiperaggiungere == "show":
        print("\n#########################")
        print("Agenda di oggi aggiornata:")
        print("#########################\n")
        for tasks in range(len(task)):
            print("·",task[tasks],"\n")
        t = 1
    elif premiperaggiungere == "close":
        t = 0
print("\n#########################")
print("Agenda di oggi aggiornata:")
print("#########################\n")
for compiti in range(len(task)):
    print("·",task[compiti],"\n")
