# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Vibecamp")

@app.get("/", response_class=HTMLResponse)
async def landing():
    return HTMLResponse("""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Vibecamp — Balance Your Flow</title>
  <meta name="description" content="VibeCamp is a community of builders, hackers, and vibecoders—where creativity meets collaboration." />
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    html { scroll-behavior: smooth; }
  </style>
</head>

<body class="bg-gray-50 text-gray-900 antialiased">
  <!-- Header -->
  <header class="w-full">
    <nav class="mx-auto max-w-6xl px-6 py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <!-- Simple Logo -->
        <svg width="36" height="36" viewBox="0 0 100 100" aria-hidden="true">
          <polygon points="50,10 90,85 10,85" fill="#2d98da"/>
          <polygon points="50,10 90,85 50,60" fill="#f1c40f"/>
          <polygon points="50,10 50,60 10,85" fill="#1b6aa5"/>
        </svg>
        <span class="font-semibold">Vibecamp</span>
      </div>
      <div class="hidden sm:flex items-center gap-6 text-sm">
        <a href="#about" class="text-gray-600 hover:text-gray-900 transition">What is Vibecamp?</a>
        <a href="#social" class="text-gray-600 hover:text-gray-900 transition">Community</a>
      </div>
    </nav>
  </header>

  <!-- Hero -->
  <section class="px-6">
    <div class="mx-auto max-w-4xl min-h-[60vh] flex flex-col items-center justify-center text-center">
      <!-- Big Logo -->
      <svg width="140" height="140" viewBox="0 0 100 100" aria-hidden="true">
        <polygon points="50,10 90,85 10,85" fill="#2d98da"/>
        <polygon points="50,10 90,85 50,60" fill="#f1c40f"/>
        <polygon points="50,10 50,60 10,85" fill="#1b6aa5"/>
      </svg>

      <h1 class="mt-6 text-4xl sm:text-5xl font-semibold">Vibecamp</h1>
      <p class="mt-2 text-lg text-gray-500">Balance Your Flow</p>

      <div class="mt-8 flex flex-col sm:flex-row gap-4">
        <a href="#about"
           class="bg-yellow-400 hover:bg-yellow-500 text-black font-medium px-8 py-3 rounded-xl transition shadow-sm hover:shadow-md">
          What is Vibecamp?
        </a>
        <a href="#social"
           class="bg-white hover:bg-gray-50 text-gray-900 font-medium px-8 py-3 rounded-xl border border-gray-200 transition shadow-sm hover:shadow-md">
          Join the Community
        </a>
      </div>
    </div>
  </section>

  <!-- What is Vibecamp -->
  <section id="about" class="px-6 py-16">
    <div class="mx-auto max-w-3xl w-full rounded-2xl border border-gray-200 bg-white p-8 shadow-sm text-gray-800">
      <h2 class="text-3xl font-semibold mb-4 text-gray-900">What is Vibecamp? 🚀</h2>
      <p class="mb-4 leading-relaxed">
        <strong>VibeCamp</strong> is a community of builders, hackers, and vibecoders — people who create not just for profit,
        but for purpose, curiosity, and joy. We believe that building is a human superpower, and that everyone deserves access to
        the tools, knowledge, and confidence to create something meaningful.
      </p>
      <p class="leading-relaxed">
        Our goal is to make “the power to build” something that scales — not through corporations or gatekeepers, but through community.
        We cultivate an ecosystem where people help each other experiment, launch, and grow ideas that build value for themselves and for others.
        VibeCamp is where creativity meets collaboration, where code meets culture, and where every builder finds their vibe.
      </p>
    </div>
  </section>

  <!-- Social / Community -->
  <section id="social" class="px-6 pb-24">
    <div class="mx-auto max-w-3xl w-full rounded-2xl border border-gray-200 bg-white p-8 shadow-sm text-gray-800">
      <h3 class="text-2xl font-semibold text-gray-900 text-center">Be part of the community</h3>

      <!-- Social Links -->
      <div class="flex flex-col sm:flex-row justify-center items-center gap-4 sm:gap-6 mt-8">
        <a href="https://www.facebook.com/groups/vibecamp" target="_blank"
           class="flex items-center gap-2 text-blue-600 hover:text-blue-800 transition">
          <i data-lucide="users"></i><span>Facebook Group</span>
        </a>

        <a href="https://www.facebook.com/profile.php?id=61579579477817" target="_blank"
           class="flex items-center gap-2 text-blue-600 hover:text-blue-800 transition">
          <i data-lucide="facebook"></i><span>Facebook Page</span>
        </a>

        <a href="https://www.meetup.com/vibecamp/" target="_blank"
           class="flex items-center gap-2 transition"
           style="color:#F64060;">
          <i data-lucide="calendar"></i><span>Meetup</span>
        </a>
      </div>

      <div class="mt-8 text-center">
        <a href="#top" class="text-yellow-600 hover:text-yellow-700 font-medium">↑ Back to Top</a>
      </div>
    </div>
  </section>

  <footer class="border-t border-gray-200 py-8 text-center text-sm text-gray-500">
    © <span id="year"></span> Vibecamp. All rights reserved.
  </footer>

  <script>
    lucide.createIcons();
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
""")
