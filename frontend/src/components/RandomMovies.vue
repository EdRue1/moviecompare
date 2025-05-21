<script setup>
import { ref, onMounted } from 'vue'

const movies = ref([])
const loading = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    const res = await fetch('/api/movies/random')
    if (!res.ok) throw new Error('Failed to fetch movies')
    movies.value = await res.json()
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div>
    <h2>Random Movies</h2>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else class="movies">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <img
          v-if="movie.poster_path"
          :src="`https://image.tmdb.org/t/p/w300${movie.poster_path}`"
          :alt="movie.title"
        />
        <h3>{{ movie.title }}</h3>
        <p><strong>Release:</strong> {{ movie.release_date }}</p>
        <p><strong>Rating:</strong> {{ movie.vote_average }}</p>
        <p>{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.movies {
  display: flex;
  gap: 2rem;
}
.movie-card {
  max-width: 300px;
}
.movie-card img {
  width: 100%;
  border-radius: 8px;
}
</style>