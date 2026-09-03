# Dictionnaire avec les différents types de logs
logs = {
    "INFO": [],
    "WARNING": [],
    "ERROR": [],
    "DEBUG": [],
    "CRITICAL": []
}

# Ouvrir le fichier en lecture
with open("exercice.txt", "r") as fichier:
    for ligne in fichier:
        for type_log in logs:
            if f"[{type_log}]" in ligne:
                logs[type_log].append(ligne.strip())


print(logs)