import argparse
from pathlib import Path
from typing import Iterable, Tuple

INITIAL_POSITION = 50
COUNTER_SIZE = 100

class CompassPointer:
    """Clase para encapsular el estado y comportamiento de la aguja."""
    def __init__(self, initial_position: int, counter_size: int):
        self.position = initial_position
        self.counter_size = counter_size
    
    def process_movement(self, direction: str, degrees: int) -> Tuple[bool, int]:
        """
        Calcula el movimiento y devuelve dos resultados independientes:
        1. bool: ¿Terminó el movimiento exactamente en el cero? (Para Parte 1)
        2. int: ¿Cuántas veces cruzó/tocó el cero durante el trayecto? (Para Parte 2)
        """
        # 1. Determinar la distancia física hasta el próximo 0 según la dirección
        if direction == 'R':
            dist_to_zero = self.counter_size - self.position
            self.position = (self.position + degrees) % self.counter_size
        elif direction == 'L':
            # Si ya estamos en 0, la distancia al próximo 0 a la izquierda es 100
            dist_to_zero = self.position if self.position != 0 else self.counter_size
            self.position = (self.position - degrees) % self.counter_size
        else:
            raise ValueError(f"Dirección desconocida: {direction}")
            
        # 2. Calcular matemáticamente cuántas veces tocó el 0 en este trayecto
        if degrees < dist_to_zero:
            zero_touches = 0
        else:
            # 1 toque inicial + cuántas vueltas completas adicionales se dieron
            zero_touches = 1 + (degrees - dist_to_zero) // self.counter_size
            
        ends_on_zero = (self.position == 0)
        
        return ends_on_zero, zero_touches

def parse_instructions(filepath: Path) -> Iterable[Tuple[str, int]]:
    with filepath.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                yield line[0], int(line[1:])

def solve(input_path: Path) -> Tuple[int, int]:
    """Resuelve ambas partes en una sola pasada para mayor eficiencia."""
    pointer = CompassPointer(initial_position=INITIAL_POSITION, counter_size=COUNTER_SIZE)
    part1_total = 0
    part2_total = 0

    for direction, degrees in parse_instructions(input_path):
        ends_on_zero, touches_in_move = pointer.process_movement(direction, degrees)
        
        if ends_on_zero:
            part1_total += 1
            
        part2_total += touches_in_move

    return part1_total, part2_total

if __name__ == '__main__':
    path = Path('Inputs/input_p1')
    p1, p2 = solve(path)
    print("Advent of code 2025, Day 1")
    print(f"Solución Parte 1: {p1}")
    print(f"Solución Parte 2: {p2}")