# music-recommender

I'll come up with a better name later. 

You'll need the Spotify Million Playlist Dataset. Read through [this website](https://research.atspotify.com/2020/09/the-million-playlist-dataset-remastered), especially on the license for usage of the dataset, and download the data in the .zip. Extract it in the root directory. 

The paper this project is based on is [An Analysis of Approaches Taken in the ACM RecSys Challenge 2018 for Automatic Music Playlist Continuation](https://dl.acm.org/doi/abs/10.1145/3344257) by Zamani et al. Specifically, it is the two-stage model by team **vl6** detailed in [Two-stage Model for Automatic Playlist Continuation at Scale](https://dl.acm.org/doi/abs/10.1145/3267471.3267480) by Volkovs et al. 

## TODO
1. implement the recommendation system in the whitepaper in a jupyter notebook
2. save that model into either weights that can be loaded and ran in Rust (webgpu?), or a callable API
3. make a website in Rust that runs the recommendations on user-input playlist