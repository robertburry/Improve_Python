# sports_sim_logic.py
import logging
import time
from data_init import generate_initial_data
from simulation import PlayoffSimulation

def team_sim_logic():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    start_time = time.time()
    teamlist, NFL, playoff_data_instance, nfc_playoffs, afc_playoffs = generate_initial_data('Modular_Example/teams_conf.csv')
    end_time = time.time()

    logging.info(f"total time taken this loop: {end_time - start_time}s \n")

    logging.info(f"AFC Playoffs are: {afc_playoffs}\n")
    logging.info(f"NFC Playoffs are: {nfc_playoffs}")

    playoff_simulator = PlayoffSimulation()

    # Simulate playoff rounds for AFC and NFC
    while len(afc_playoffs) > 1:
        afc_playoffs = playoff_simulator.simulate_playoff_round(afc_playoffs)

    while len(nfc_playoffs) > 1:
        nfc_playoffs = playoff_simulator.simulate_playoff_round(nfc_playoffs)
    
    # afc_champion = playoff_simulator.simulate_playoff_round(afc_playoffs)
    # nfc_champion = playoff_simulator.simulate_playoff_round(nfc_playoffs)

    print(f"\nAFC Champion: {afc_playoffs[0][0]} Ranked: {afc_playoffs[0][1]}")
    print(f"NFC Champion: {nfc_playoffs[0][0]} Ranked: {nfc_playoffs[0][1]}")

    league_championship = [(afc_playoffs[0][0], afc_playoffs[0][1]), (nfc_playoffs[0][0], nfc_playoffs[0][1])]

    league_champion = playoff_simulator.simulate_playoff_round(league_championship)

    print(f"League Champion: {league_champion[0][0]} Ranked: {league_champion[0][1]}")
