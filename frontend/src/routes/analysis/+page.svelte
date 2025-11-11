<script lang="ts">
  import { onMount } from 'svelte'
  import axios from 'axios'
  import { DarkMode, P, Heading, Sidebar, Img, Accordion, AccordionItem, Button } from 'flowbite-svelte'
  import { page } from '$app/stores'
  import { SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte'
  import { ChartPieSolid, ColumnSolid, HomeSolid } from 'flowbite-svelte-icons'

  $: activeUrl = $page.url.pathname;

  let protonTop = ''
  let bmwTop: string = '';
  let bmwLeast: string = '';
  let brz86: string = '';
  let toyotaSubaru_CumulativeGrowth: string = '';
  let germanCarGrowth: string = '';
  let supercarGrowth: string = '';
  const items = Array(6).fill(false);

  const open_all = () => items.forEach((_, i) => (items[i] = true));
  const close_all = () => items.forEach((_, i) => (items[i] = false));

  onMount(async () => {
    const apiBaseUrl = 'http://127.0.0.1:5000';

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

    protonTop                     = await fetchImage('/api/proton/top');
    bmwTop                        = await fetchImage('/api/bmw/top');
    bmwLeast                      = await fetchImage('/api/bmw/least');
    brz86                         = await fetchImage('/api/brz_86');
    toyotaSubaru_CumulativeGrowth = await fetchImage('/api/cumulative_growth');
    germanCarGrowth               = await fetchImage('/api/german_cars');
    supercarGrowth                =  await fetchImage('/api/supercars');

  });
</script>

<body class="bg-white dark:bg-gray-800">

  <div id="sidebar" class="z-50 p-4 bg-white dark:bg-gray-800 w-64 fixed inset-y-0 left-0  pb-32">
    <Sidebar {activeUrl}>
      <SidebarWrapper>
        <SidebarGroup>
          <SidebarItem label="Home" href="../">
            <svelte:fragment slot="icon">
              <HomeSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
            </svelte:fragment>
          </SidebarItem>
          <SidebarItem label="Analysis" href='/analysis'>
            <svelte:fragment slot="icon">
              <ColumnSolid class="w-6 h-6 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" />
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
  
  <div class="flex px-4 mx-auto w-full">
    <main class="lg:ml-72 w-full mx-auto">
      <DarkMode />

      <!-- Description -->
      <Heading tag="h1" class="mx-4 w-full p-5" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
        Exploratory Data Analysis
      </Heading>
      <P>This part of the data is preprocess at the backend using python's numpy, pandas, matplotlib, and seaborn library</P>

      <!-- Utility button -->
      <Button class="my-6 mr-3" on:click={open_all} >Open all</Button>
      <Button on:click={close_all}>Close all</Button>

      <!-- Accordion Component -->
      <Accordion multiple>
        <AccordionItem  bind:open={items[0]}>
          <span slot="header">BMW Top</span>
          <Heading tag="h4" class="my-2">BMW Most Registered Models</Heading>
          <div class="pt-7">
            {#if bmwTop}
              <Img src={bmwTop} alt="Top BMW Models (2015-2025)" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[1]}>
          <span slot="header">BMW Least </span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">BMW Least Registered Models</Heading>
            {#if bmwLeast}
              <Img src={bmwLeast} alt="Least Registered BMW Models (2015-2025)" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[2]}>
          <span slot="header">Subaru vs Toyota</span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">BRZ vs 86 vs GR86</Heading>
            {#if brz86}
              <Img src={brz86} alt="Subaru BRZ vs Toyota 86 vs Toyota GR86" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[3]}>
          <span slot="header">Total of BRZ vs 86 vs GR86</span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">Cumulative Growth of Subaru BRZ, Toyota 86 and Toyota GR86</Heading>
            {#if toyotaSubaru_CumulativeGrowth}
              <Img src={toyotaSubaru_CumulativeGrowth} alt="Cumulative Growth of Subaru BRZ, Toyota 86 and Toyota GR86" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[4]}>
          <span slot="header">Growth German Cars</span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">Cumulative Growth Audi, BMW, Mercedes Top 3 Models</Heading>
            {#if germanCarGrowth}
              <Img src={germanCarGrowth} alt="Cumulative Growth Audi, BMW, Mercedes Top 3 Models" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[5]}>
          <span slot="header">Supercars Growth</span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">Cumulative Growth Ferrari, Lamborghini, Mclaren Top 3 Models</Heading>
            {#if supercarGrowth}
              <Img src={supercarGrowth} alt="Cumulative Growth Audi, BMW, Mercedes Top 3 Models" />
            {/if}
          </div>
        </AccordionItem>
        <AccordionItem bind:open={items[6]}>
          <span slot="header">Proton's Registration</span>
          <div class="py-2">
            <Heading tag="h4" class="my-2">Top 10 Proton Models Registrations after 2020</Heading>
            {#if protonTop}
              <Img src={protonTop} alt="Top 10 Proton Models Registrations" />
            {/if}
          </div>
        </AccordionItem>
      </Accordion>
    </main>
  </div>
</body>
