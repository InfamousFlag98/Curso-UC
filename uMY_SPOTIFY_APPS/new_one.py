import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_playlist_id_by_name(sp, playlist_name):
    playlists = sp.current_user_playlists()["items"]
    for pl in playlists:
        if pl['name'].lower() == playlist_name.lower():
            return pl['id']
    return None

def search_tracks(sp, track_names):
    track_uris = []
    for track in track_names:
        results = sp.search(q=track, type="track", limit=1)
        if results["tracks"]["items"]:
            uri = results["tracks"]["items"][0]["uri"]
            track_uris.append(uri)
    return track_uris

def add_tracks_to_playlist(sp, playlist_id, track_uris):
    for i in range(0, len(track_uris), 100):
        sp.playlist_add_items(playlist_id, track_uris[i:i+100])

def remove_tracks_from_playlist(sp, playlist_id, track_uris):
    for i in range(0, len(track_uris), 100):
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris[i:i+100])

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="09bc176f84244209be398249260411e3",
        client_secret="79feeb85be2949b18bc2bb91ae88ce8c",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-public playlist-modify-private"
    ))

    user_id = sp.current_user()["id"]

    print("ESCOLHA UMA OPÇÃO: ")
    print("1. Criar uma nova playlist")
    print("2. Adicionar faixas a uma playlist existente")
    print("3. Obter um ID de playlist pelo nome")
    print("4. Remover faixas específicas de uma playlist")
    print("5. Excluir (deletar) uma playlist")
    choice = input("Digite o número da sua escolha: ")

    if choice == "1":
        playlist_name = input("Digite o nome da nova playlist: ")
        description = input("Digite uma descrição (opcional): ")
        public_choice = input("A playlist será pública? (s/n): ").strip().lower()
        public = True if public_choice == 's' else False
        playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=public, description=description)
        playlist_id = playlist["id"]
        print("Digite os nomes das faixas (uma por linha). Digite uma linha em branco para terminar:")
        track_names = []
        while True:
            track = input()
            if not track:
                break
            track_names.append(track)
        track_uris = []
        for track in track_names:
            results = sp.search(q=track, type="track", limit=1)
            if results["tracks"]["items"]:
                uri = results["tracks"]["items"][0]["uri"]
                track_uris.append(uri)
        for i in range(0, len(track_uris), 100):
            sp.playlist_add_items(playlist_id, track_uris[i:i+100])
        print(f"Playlist '{playlist_name}' criada e sincronizada!")

    elif choice == "2":
        playlist_name = input("Digite o nome da playlist existente: ")
        playlist_id = get_playlist_id_by_name(sp, playlist_name)
        if not playlist_id:
            print("Playlist não encontrada.")
            return
        print("Digite os nomes das faixas a serem adicionadas (uma por linha). Digite uma linha em branco para terminar:")
        track_names = []
        while True:
            track = input()
            if not track:
                break
            track_names.append(track)
        track_uris = []
        for track in track_names:
            results = sp.search(q=track, type="track", limit=1)
            if results["tracks"]["items"]:
                uri = results["tracks"]["items"][0]["uri"]
                track_uris.append(uri)
        for i in range(0, len(track_uris), 100):
            sp.playlist_add_items(playlist_id, track_uris[i:i+100])
        print("Faixas adicionadas à playlist.")

    elif choice == "3":
        playlist_name = input("Digite o nome da playlist: ")
        playlist_id = get_playlist_id_by_name(sp, playlist_name)
        if playlist_id:
            print(f"ID da playlist '{playlist_name}': {playlist_id}. Quer abrir a playlist no navegador? (s/n)")
            open_choice = input().strip().lower()
            if open_choice == 's':
                import webbrowser
                webbrowser.open(f"https://open.spotify.com/playlist/{playlist_id}")
            print()
        else:
            print("Playlist não encontrada.")

    elif choice == "4":
        playlist_name = input("Digite o nome da playlist: ")
        playlist_id = get_playlist_id_by_name(sp, playlist_name)
        if not playlist_id:
            print("Playlist não encontrada.")
            return
        print("Digite os nomes das faixas a serem removidas (uma por linha). Digite uma linha em branco para terminar:")
        track_names = []
        while True:
            track = input()
            if not track:
                break
            track_names.append(track)
        track_uris = search_tracks(sp, track_names)
        remove_tracks_from_playlist(sp, playlist_id, track_uris)
        print("Faixas removidas da playlist.")
    elif choice == "5":
        playlist_name = input("Digite o nome da playlist que deseja limpar e tornar privada: ")
        playlist_id = get_playlist_id_by_name(sp, playlist_name)
        if not playlist_id:
            print("Playlist não encontrada.")
            return
        # Buscar todas as faixas da playlist
        tracks = []
        results = sp.playlist_items(playlist_id, fields="items.track.uri,total", additional_types=['track'])
        tracks.extend([item['track']['uri'] for item in results['items'] if item['track']])
        # Paginação se necessário
        while results.get('next'):
            results = sp.next(results)
            tracks.extend([item['track']['uri'] for item in results['items'] if item['track']])
        if tracks:
            remove_tracks_from_playlist(sp, playlist_id, tracks)
            print("Todas as faixas foram removidas da playlist.")
        else:
            print("A playlist já está vazia.")
        # Tornar a playlist privada
        sp.playlist_change_details(playlist_id, public=False)
        print(f"Playlist '{playlist_name}' agora está vazia e privada!")
    
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()