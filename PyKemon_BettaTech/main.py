from constants import *
from models import *

# Define pokemons with its stats

pokemon1 = Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = Pokemon("Charmander", 100, "fire", None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

# /-----------------------STATS------------------------------/
pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}


# /-----------------------ATTACKS------------------------------/
pokemon1.attacks = [Attack(
    "scratch", "normal", PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack(
    "scratch", "normal", PHYSICAL, 10, 10, 100)]



def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK -> attack 0
        tmp_command = input(f"What should {pokemon.name} do?\n").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command(
                        {DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


# /------------------START_BATTLE--------------------------/
battle = Battle(pokemon1, pokemon2)

while not battle.is_finished():
    # First ask for command
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()
