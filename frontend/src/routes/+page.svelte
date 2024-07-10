<script>
    import { P, A, Heading, DarkMode, Sidebar } from 'flowbite-svelte';
    import { SidebarGroup, SidebarItem, SidebarWrapper } from 'flowbite-svelte';
    import { ChartPieSolid, ColumnSolid, HomeSolid } from 'flowbite-svelte-icons';
    import { page } from '$app/stores';

    $: activeUrl = $page.url.pathname;

</script>



<!-- src/app.html -->
<body class="bg-white dark:bg-gray-800">

    <div id="sidebar" class="z-50 p-4 bg-white dark:bg-gray-800 w-64 fixed inset-y-0 left-0 pb-32" aria-labelledby="sidebar">
        <Sidebar {activeUrl}>
            <SidebarWrapper>
              <SidebarGroup>
                <SidebarItem label="Home" href="/">
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

            <Heading tag="h1" class="mx-4 w-full p-5" customSize="text-4xl font-extrabold  md:text-5xl lg:text-6xl">
                Malaysia Car Analysis
            </Heading>
            <P class="mb-6 text-lg lg:text-xl sm:px-16 xl: dark:text-gray-400">
                Looking on all car makers statistics in Malaysia
            </P>
            <A class="mb-6 text-lg lg:text-xl sm:px-16 xl: dark:text-green-400" 
                href='/analysis'
                >
                See the data
            </A>
        </main>
        
    </div>

</body>
  