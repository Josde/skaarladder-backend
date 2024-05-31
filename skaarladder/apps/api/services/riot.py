from typing import List
from django.conf import settings
from models import Player
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from utils.constants import API_CLIENT_ARGS, SOLOQ, SOLOQ_INT

async def fetch_player_data(player : Player) -> RiotAPISchema.LolSummonerV4Summoner:
    async with RiotAPIClient(API_CLIENT_ARGS) as client:
        if not player.puuid: # First run - player is only identified by their name.
            result = await client.get_lol_summoner_v4_by_name(region=player.region, name=player.name)
        else: 
            result = await client.get_lol_summoner_v4_by_puuid(region=player.region, puuid=player.puuid)
        return result
        
    
async def fetch_player_ranked_data(player : Player, queue : str = SOLOQ) -> RiotAPISchema.LolLeagueV4LeagueFullEntry: 
    async with RiotAPIClient(API_CLIENT_ARGS) as client:
        queue_data = await client.get_lol_league_v4_entries_by_summoner(region=player.region, summoner_id=player.summoner_id)
        result = filter(lambda item: item.queueType == queue, queue_data)
        if result: 
            return result[0]
        return None

async def fetch_player_match_history_details(player : Player, start: int = 0, count : int = 10, queue: int = SOLOQ_INT) -> List[RiotAPISchema.LolMatchV5Match]:
    async with RiotAPIClient(API_CLIENT_ARGS) as client:
        match_ids = await client.get_lol_match_v5_match_ids_by_puuid(region=player.region, puuid=player.puuid, queries={"start": start, "count": count})
        result = []
        for id in match_ids:
            match = await client.get_lol_match_v5_match(region=player.region, id=id)
            result.append(match)
        return result

async def fetch_player_streak(player : Player, queue: int = SOLOQ_INT) -> int:
    result = last_result = None
    streak = 0
        
    matches = await fetch_player_match_history_details(player=player, count=settings.MAX_STREAK_FETCH_COUNT)
    
    for match in matches:
        if (result != last_result) and last_result is not None:
            break
        won = await get_match_result(player, match)
        last_result = result
        result = won
        if result == last_result:
            streak += 1 if won else -1

    return streak

async def get_match_result(player: Player, match: RiotAPISchema.LolMatchV5Match) -> bool:
    teams = match.info.teams
    participants = match.metadata.participants
    our_player_as_participant = filter(lambda participant: participant.puuid == player.puuid, participants)[0]
    for team in teams:
        if team.teamId == our_player_as_participant.teamId:
            return team.win