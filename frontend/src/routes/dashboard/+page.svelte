<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';
	import { DarkMode, P, Heading, Sidebar } from 'flowbite-svelte';
  import { page } from '$app/stores';
  import { SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
  import { ChartPieSolid, HomeSolid } from 'flowbite-svelte-icons';

  $: activeUrl = $page.url.pathname;

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

  <div id="sidebar" class="z-50 p-4 bg-white dark:bg-gray-800 w-64 fixed inset-y-0 left-0  pb-32">
    <Sidebar {activeUrl}>
      <SidebarWrapper>
        <SidebarGroup>
          <SidebarItem label="Home" href="../">
            <svelte:fragment slot="icon">
              <HomeSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            </svelte:fragment>
          </SidebarItem>
          <SidebarItem label="Dashboard" href='/dashboard'>
            <svelte:fragment slot="icon">
              <ChartPieSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            </svelte:fragment>
          </SidebarItem>
        </SidebarGroup>
      </SidebarWrapper>
    </Sidebar>
  </div>
  
</body>
