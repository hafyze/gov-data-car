<script lang="ts">
  import { onMount } from 'svelte';

  interface CarMaker {
    id: number;
    name: string;
  }

  let carmakers: CarMaker[] = [];

  onMount(async () => {
    try {
      const response = await fetch('http://localhost:5000/api/carmakers');
      if (response.ok) {
        carmakers = await response.json();
      } else {
        console.error('Failed to fetch car makers:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  });
</script>

<h1>Car Makers</h1>
<ul>
  {#each carmakers as carmaker}
    <li>{carmaker.name}</li>
  {/each}
</ul>
