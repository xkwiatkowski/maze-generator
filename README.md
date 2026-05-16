# Generowanie labiryntu algorytmami grafowymi

## Tematyka
Projekt polega na implementacji generatora labiryntów z wykorzystaniem algorytmów grafowych. Labirynt jest reprezentowany jako graf siatki (komórki = wierzchołki, ściany = krawędzie), a generowanie polega na budowaniu losowego drzewa rozpinającego. Projekt obejmuje wizualizację działania algorytmów oraz porównanie własności wygenerowanych labiryntów.

## Algorytmy
- Randomized Kruskal's Algorithm (z wykorzystaniem struktury Union-Find/DSU)
- Randomized Prim's Algorithm

## Materiały
- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

## Technologie
- Python 3
- Własna implementacja algorytmów i struktury Union-Find
- Wizualizacja krok po kroku w Pygame

## Uruchomienie
```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
python3 main.py
```