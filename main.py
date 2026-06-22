def main():
    import json
    from pathlib import Path
    from scipy import sparse
    from tqdm import tqdm

    SEED = 48635
    NUM_SONGS = 2_262_292 # NOTE: this is taken from the provided stats.py file.
                        # this could be counted on-the-fly, preferably with a better algorithm,
                        # if this is going to be deployed more generally. 
    NUM_PLAYLISTS = 1_000_000

    # Load slices to memory
    spotify_mpd = Path("spotify_million_playlist_dataset")
    playlists_path = spotify_mpd / "data"
    slice_paths = list(playlists_path.glob(r"*.json"))

    # Keep a hashmap of:
    # playlist ID -> integer index
    # track ID -> integer index
    plists = set()
    tracks = {}
    plist_tracks_matrix = sparse.csr_matrix((NUM_PLAYLISTS, NUM_SONGS))

    unique_songs = 0
    for spth in tqdm(slice_paths, desc = "slices", position = 0): # for each slice json,
        with open(spth, 'r') as f: # open the file
            slice = json.load(f) # load the data
            for i, plist in tqdm(enumerate(slice["playlists"]), desc = "playlists in slice", position = 1, leave = False): # and for each playlist in the json,
                plists.add(plist["pid"]) # record the PID (and index)
                for j, track in enumerate(plist["tracks"]): # and for each song in the playlist,
                    # TODO: this checks the whole historic list of songs for each new song
                    # extremely slow, should be improved. 
                    if track["track_uri"] not in tracks: # if we haven't seen this song yet,
                        tracks["track_uri"] = unique_songs # save the new index
                        plist_tracks_matrix[i, unique_songs] = 1 # and log the instance in the CSR matrix
                        unique_songs += 1
                    else:
                        song_index = tracks["track_uri"]
                        plist_tracks_matrix[i, song_index] = 1


if __name__ == "__main__":
    main()
