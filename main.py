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
  <title>Vibecamp</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 text-gray-900 flex flex-col items-center justify-center min-h-screen px-4">
  <div class="flex flex-col items-center text-center">
    <!-- Logo -->
    <svg width="120" height="120" viewBox="0 0 100 100" aria-hidden="true">
      <polygon points="50,10 90,85 10,85" fill="#2d98da"/>
      <polygon points="50,10 90,85 50,60" fill="#f1c40f"/>
      <polygon points="50,10 50,60 10,85" fill="#1b6aa5"/>
    </svg>

    <!-- Title & Tagline -->
    <h1 class="mt-6 text-4xl font-semibold">Vibecamp</h1>
    <p class="mt-2 text-lg text-gray-500">Balance Your Flow</p>

    <!-- Button -->
    <a href="/what-is-vibecamp"
       class="mt-8 bg-yellow-400 hover:bg-yellow-500 text-black font-medium px-8 py-3 rounded-xl transition shadow-sm hover:shadow-md">
      What is Vibecamp?
    </a>
  </div>
</body>
</html>
""")

@app.get("/what-is-vibecamp", response_class=HTMLResponse)
async def what_is_vibecamp():
    return HTMLResponse("""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>What is Vibecamp?</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 flex items-center justify-center min-h-screen px-6">
  <div class="max-w-3xl w-full rounded-2xl border border-gray-200 bg-white p-8 shadow-sm text-gray-800">
    <h1 class="text-3xl font-semibold mb-4 text-gray-900">What is Vibecamp? 🚀</h1>
    <p class="mb-4 leading-relaxed">
      <strong>VibeCamp</strong> is a community of builders, hackers, and vibecoders — people who create not just for profit, but for purpose, curiosity, and joy. 
      We believe that building is a human superpower, and that everyone deserves access to the tools, knowledge, and confidence to create something meaningful.
    </p>
    <p class="leading-relaxed">
      Our goal is to make “the power to build” something that scales — not through corporations or gatekeepers, but through community. 
      We want to cultivate an ecosystem where people help each other experiment, launch, and grow ideas that build value for themselves and for others. 
      VibeCamp is where creativity meets collaboration, where code meets culture, and where every builder finds their vibe.
    </p>
    <div class="mt-8 text-center">
      <a href="/" class="text-yellow-600 hover:text-yellow-700 font-medium">← Back to Home</a>
    </div>
  </div>
</body>
</html>
""")
