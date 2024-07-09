<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';
	import { DarkMode, P, Heading } from 'flowbite-svelte';

  let bmwTop: string = '';
  let bmwLeast: string = '';
  let brz86: string = '';
  let cumulativeGrowth: string = '';

  onMount(async () => {
      const apiBaseUrl = 'http://127.0.0.1:5000'

      const fetchImage = async (endpoint: string): Promise<string> => {
          try {
              const response = await axios.get(`${apiBaseUrl}${endpoint}`, { responseType: 'blob' });
              const imageBlob = response.data;
              return URL.createObjectURL(imageBlob);
          } catch (error) {
              console.error(`Error fetching image from ${endpoint}:`, error);
              return '';
          }
      };

      bmwTop = await fetchImage('/api/bmw/top');
      bmwLeast = await fetchImage('/api/bmw/least');
      brz86 = await fetchImage('/api/brz_86');
      cumulativeGrowth = await fetchImage('/api/cumulative_growth');
  });
</script>

<body class="bg-white dark:bg-gray-800">
  <DarkMode />

  <Heading tag="h1" class="m-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
    BMW Top Models
  </Heading>
  {#if bmwTop}
      <img src={bmwTop} alt="Top BMW Models (2015-2024)">
  {/if}

  <Heading tag="h1" class="m-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
    BMW Least Registered Models
  </Heading>
  {#if bmwLeast}
      <img src={bmwLeast} alt="Least Registered BMW Models (2015-2024)">
  {/if}

  <Heading tag="h1" class="m-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
    Subaru BRZ vs Toyota 86 vs Toyota GR86
  </Heading>
  {#if brz86}
      <img src={brz86} alt="Subaru BRZ vs Toyota 86 vs Toyota GR86">
  {/if}

  <Heading tag="h1" class="m-4" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
    Cumulative Growth of Subaru BRZ, Toyota 86 and Toyota GR86
  </Heading>
  {#if cumulativeGrowth}
      <img src={cumulativeGrowth} alt="Cumulative Growth of Subaru BRZ, Toyota 86 and Toyota GR86">
  {/if}
</body>
