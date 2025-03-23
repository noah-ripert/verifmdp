import hashlib
import requests

def check_password(password):
    # Convertir le mot de passe en hash SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Extraire les 5 premiers caractères du hash
    first5_chars = sha1_hash[:5]

    # L'URL de l'API Have I Been Pwned
    url = f'https://api.pwnedpasswords.com/range/{first5_chars}'

    # Faire une requête GET à l'API
    response = requests.get(url)

    if response.status_code == 200:
        # L'API retourne une liste de hash avec le nombre d'occurrences
        hashes = response.text.splitlines()

        # Vérifier si notre hash fait partie des résultats
        for hash_entry in hashes:
            # Comparer les 35 caractères restants du hash
            hash_suffix, count = hash_entry.split(':')
            if sha1_hash[5:].upper() == hash_suffix:
                return f"Le mot de passe a été compromis {count} fois. Choisissez-en un autre."
        
        return "Le mot de passe n'a pas été compromis dans des fuites de données."
    else:
        return "Erreur lors de la vérification du mot de passe."

if __name__ == "__main__":
    password = input("Entrez un mot de passe à vérifier : ")
    result = check_password(password)
    print(result)

    
