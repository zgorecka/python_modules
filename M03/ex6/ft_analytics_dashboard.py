def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    data = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
        ],
    }

    players = data["players"]
    sessions = data["sessions"]

    print("=== List Comprehension Examples ===")

    high_level_players = [
        name for name, info in players.items()
        if info["level"] > 30
    ]
    print("High level players (>30):", high_level_players)

    completed_scores = [
        session["score"] for session in sessions
        if session["completed"]
    ]
    print("Completed session scores:", completed_scores)

    long_sessions = [
        session for session in sessions
        if session["duration_minutes"] > 60
    ]
    print("Long sessions (>60 min):", long_sessions)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        name: info["total_score"]
        for name, info in players.items()
    }
    print("Player scores:", player_scores)

    level_category = {
        name: (
            "high" if info["level"] > 30
            else "medium" if info["level"] > 15
            else "low"
        )
        for name, info in players.items()
    }
    print("Level categories:", level_category)

    sessions_per_player = {
        name: len([
            s for s in sessions
            if s["player"] == name
        ])
        for name in players
    }
    print("Sessions per player:", sessions_per_player)

    print("\n=== Set Comprehension Examples ===")

    unique_modes = {
        session["mode"]
        for session in sessions
    }
    print("Unique modes used:", unique_modes)

    players_completed = {
        session["player"]
        for session in sessions
        if session["completed"]
    }
    print("Players with completed sessions:", players_completed)

    unique_achievement_counts = {
        info["achievements_count"]
        for info in players.values()
    }
    print("Unique achievement counts:", unique_achievement_counts)

    print("\n=== Combined Analysis ===")

    total_players = len(players)
    total_sessions = len(sessions)

    average_session_score = sum(
        session["score"] for session in sessions
    ) / total_sessions

    def get_total_score(player_name: str) -> int:
        return players[player_name]["total_score"]

    def get_session_duration(session: dict) -> int:
        return session["duration_minutes"]

    top_player = max(players, key=get_total_score)

    shortest_session = min(sessions, key=get_session_duration)

    print("Total players:", total_players)
    print("Total sessions:", total_sessions)
    print("Average session score:", average_session_score)
    print("Top performer:", top_player,
          f"({players[top_player]['total_score']} points)")
    print("Shortest session:", shortest_session)


if __name__ == "__main__":
    main()
