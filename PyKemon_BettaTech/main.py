import constants
import models

# Define pokemons with its stats

pokemon1 = models.Pokemon("Bulbasaur", 100, "grass", "poison")
pokemon2 = models.Pokemon("Charmander", 100, "fire", None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

# /-----------------------STATS------------------------------/
pokemon1.stats = {
    constants.HP: 45,
    constants.ATTACK: 49,
    constants.DEFENSE: 49,
    constants.SPATTACK: 65,
    constants.SPDEFENSE: 65,
    constants.SPEED: 45
}

pokemon2.stats = {
    constants.HP: 39,
    constants.ATTACK: 52,
    constants.DEFENSE: 43,
    constants.SPATTACK: 80,
    constants.SPDEFENSE: 65,
    constants.SPEED: 65
}


# /-----------------------ATTACKS------------------------------/
pokemon1.attacks = [models.Attack(
    "scratch", "normal", constants.PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [models.Attack(
    "scratch", "normal", constants.PHYSICAL, 10, 10, 100)]



def ask_command(pokemon):
    command = None
    while not command:
        # DO ATTACK -> attack 0
        tmp_command = input(f"What should {pokemon.name} do?\n").split(" ")
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == constants.DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = models.Command(
                        {constants.DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


# /------------------START_BATTLE--------------------------/
battle = models.Battle(pokemon1, pokemon2)

while not battle.is_finished():
    # First ask for command
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = models.Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()
