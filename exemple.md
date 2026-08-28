# Calcul de distance entre les centre de deux communes

## Vision globale
**entrée:** code Insee des deux communes -> chaines de 5 caractères

**sortie:** distance en km -> nombre réel

## Etapes
1. récupérer les coordonnées de la première commune
  - **entree:** code de la commune
  - **sortie:** longitude, latitude
2. récupérer les coordonnées de la seconde commune
  - **entree:** code de la commune
  - **sortie:** longitude, latitude
3. calculer la distance
  - **entree:** deux couples de coordonnées
  - **sortie:** distance en km


# Exemple d'implémentation

```mermaid

classDiagram
  class Coordonnees{
      - longitude: double
      - latitude: double
      + double distance_a(c: Coordonnees) double
  }
  class Commune{
    - CodeInsee : str
    - Nom : str
    + donne_coordonnees() Coordonnes
  }
  class Commune_DAO{
    + donne_commune(code: str) Commune
  }
  class Service{
    + distance_centre_communes(code1: str, code2:str) double
  }
  
  Commune *--> "1" Coordonnees  : centre_commune
  Commune_DAO *--> "*" Commune
  Service --> Commune_DAO
```

```mermaid

sequenceDiagram
    Service->>Commune_DAO: donne_commune(code1)
    Commune_DAO-->>Service: Commune:com1
    Service->>Commune_DAO: donne_commune(code2)
    Commune_DAO-->>Service: Commune:com1
    Service->>com1: donne_coordonnees
    com1-->>Service: coor1
    Service->>com2: donne_coordonnees
    com2-->>Service: coor2
    Service->>coor1 : distance_a(coord2)
    coor1-->>Service: resultat

```
