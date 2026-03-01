import sys
import time
import gc
import tracemalloc


strong_matches = [
    # Student Life
    ("graduate thesis research", "college study academia"),
    ("student loan budget frugal", "finance saving minimalist"),
    ("campus internship networking resume", "career job hunting professional"),
    ("study group notes exam", "tutoring academic college"),
    # Gamer Scenarios
    ("fps shooter competitive ranked", "esports gaming tournament"),
    ("streaming twitch content", "youtube vlog editing creator"),
    ("rpg open-world exploration lore", "fantasy worldbuilding adventure quest"),
    ("speedrun challenge achievement grinding", "competitive gaming esports ranked"),
    ("pc build hardware specs", "gaming setup rgb peripherals"),
    # Fitness & Health
    ("marathon running trails endurance", "cycling outdoor cardio endurance"),
    ("powerlifting barbell strength", "gym protein bodybuilding supplements"),
    ("crossfit hiit circuit training", "fitness gym workout endurance"),
    ("swimming laps aquatic", "triathlon endurance cardio outdoor"),
    # Food Lovers
    ("street food travel eating", "foodie cuisine culture exploring"),
    ("meal prep macros diet tracking", "fitness gym nutrition bodybuilding"),
    ("wine tasting vineyard pairing", "food culture travel gastronomy"),
    ("ramen noodles japanese cuisine", "foodie asian cooking culture"),
    # Travel
    ("solo backpacker budget hostel", "travel adventure exploring wanderlust"),
    ("digital nomad remote work cafe", "freelance coding travel laptop"),
    ("road trip van camping", "adventure outdoor nature wilderness"),
    ("culture history museum sightseeing", "travel exploration heritage landmarks"),
    # Creative Types
    ("drawing illustration digital-art", "design ui ux creative"),
    ("writing fiction novel storytelling", "books reading fantasy scifi"),
    ("film directing cinematography", "screenwriting storytelling narrative"),
    ("graphic design typography branding", "illustration art creative digital"),
    # Tech People
    ("open-source linux terminal cli", "coding developer software engineer"),
    ("machine-learning data python notebooks", "research academia statistics modeling"),
    ("devops cloud infrastructure docker", "backend engineering deployment sysadmin"),
    ("mobile app swift kotlin", "software developer product startup"),
    # Wellness & Mindfulness
    ("meditation journaling therapy self-care", "mindfulness mental-health wellness"),
    (
        "reading philosophy stoicism marcus-aurelius",
        "self-improvement books journaling",
    ),
    ("sleep routine recovery health", "wellness mindfulness self-care balance"),
    ("nature walks forest bathing", "outdoor hiking peace solitude"),
]

partial_matches = [
    # Student Life
    ("dorm cooking microwave ramen", "easy recipes budget meal-prep"),
    ("campus club volleyball social", "sports team outdoor activities"),
    ("graduate thesis research writing", "books reading fiction storytelling"),
    ("student budget finance frugal", "crypto investing trading stocks"),
    # Gamer Scenarios
    ("indie games pixel retro", "nostalgia 8bit classic console cartridge"),
    ("rpg lore worldbuilding fantasy", "books writing fiction"),
    ("streaming twitch gaming content", "podcasting audio creator storytelling"),
    ("mobile gaming casual puzzle", "esports competitive fps ranked"),
    # Fitness & Health
    ("vegan plant-based nutrition cooking", "cooking healthy organic recipes"),
    ("yoga breathwork flexibility", "marathon running crossfit hiit"),
    ("hiking trails nature outdoor", "gym workout bodybuilding lifting"),
    ("sports basketball pickup games", "esports competitive gaming ranked"),
    # Food Lovers
    ("baking sourdough bread pastry", "cooking recipes kitchen meals"),
    ("coffee espresso barista latte-art", "cafe aesthetic reading journaling"),
    ("meal prep diet macros", "vegan plant-based nutrition organic"),
    ("bbq grilling meat outdoor", "camping outdoor cooking adventure"),
    # Travel
    ("roadtrip camping van-life", "outdoor hiking nature photography"),
    ("luxury resort spa vacation", "travel foodie culture city-trips"),
    ("travel photography landscape", "photography portrait studio editing"),
    ("culture history sightseeing", "reading history books nonfiction"),
    # Creative Types
    ("photography street urban documentary", "film vintage analog darkroom"),
    ("music producer beats sampling", "dj nightlife electronic rave"),
    ("writing fiction novel", "screenwriting film directing narrative"),
    ("illustration character-design", "tattoo art ink body-art"),
    # Tech People
    ("startup founder pitch investor", "entrepreneur business networking"),
    ("cybersecurity hacking ctf", "networking sysadmin linux"),
    ("data science python analytics", "finance trading algorithms quant"),
    ("ux design user-research prototyping", "graphic design branding visual"),
    # Wellness & Mindfulness
    ("astrology tarot spiritual", "crystals meditation energy healing"),
    ("hiking nature forest solitude", "meditation mindfulness breathwork"),
    ("self-improvement productivity habits", "reading philosophy stoicism"),
    ("therapy mental-health journaling", "yoga breathwork meditation"),
]

mismatches = [
    ("esports competitive fps ranked", "yoga meditation breathwork spiritual"),
    ("luxury resort spa fashion", "camping van-life hiking trails"),
    ("crypto trading defi blockchain", "cooking baking sourdough recipes"),
    ("metal band guitar concert mosh", "astrology tarot crystals spiritual"),
    ("powerlifting barbell gym", "indie film arthouse cinema philosophy"),
    ("startup pitch fundraising", "anime cosplay manga collector figurines"),
    ("knitting crochet yarn crafts", "esports fps competitive gaming"),
    ("birdwatching nature journaling quiet", "nightlife clubbing rave electronic"),
    ("chess strategy tournament board-games", "surfing beach ocean waves"),
    ("opera classical-music symphony", "streetwear hype sneakers fashion drops"),
    ("gardening plants soil homestead", "cryptocurrency nft blockchain trading"),
    ("woodworking carpentry tools handcraft", "kpop idol fandom concert merch"),
    ("sailing yacht ocean navigation", "vegan cooking recipes plant-based"),
    ("tabletop rpg dungeons-dragons board-games", "crossfit gym lifting protein"),
]

word_pairs_with_scores = [
    # Animals
    ("cat", "dog", 0.6),
    ("wolf", "fox", 0.65),
    ("lion", "tiger", 0.75),
    ("eagle", "hawk", 0.85),
    ("shark", "whale", 0.55),
    ("rabbit", "hare", 0.90),
    ("horse", "donkey", 0.70),
    ("crow", "raven", 0.88),
    ("frog", "toad", 0.85),
    ("ant", "bee", 0.60),
    # Royalty / Authority
    ("king", "queen", 0.88),
    ("prince", "princess", 0.90),
    ("emperor", "empress", 0.90),
    ("lord", "lady", 0.85),
    ("knight", "soldier", 0.65),
    # Fruits / Food
    ("apple", "orange", 0.75),
    ("grape", "cherry", 0.70),
    ("bread", "butter", 0.65),
    ("rice", "wheat", 0.70),
    ("milk", "cheese", 0.72),
    ("lemon", "lime", 0.88),
    ("coffee", "tea", 0.78),
    ("sugar", "salt", 0.60),
    # Vehicles
    ("car", "bicycle", 0.55),
    ("train", "bus", 0.65),
    ("boat", "ship", 0.85),
    ("plane", "helicopter", 0.70),
    ("motorcycle", "scooter", 0.82),
    ("truck", "van", 0.72),
    # Shelter / Place
    ("house", "home", 0.95),
    ("apartment", "condo", 0.88),
    ("castle", "fortress", 0.80),
    ("cabin", "cottage", 0.85),
    ("hotel", "motel", 0.88),
    ("office", "workplace", 0.90),
    ("school", "university", 0.78),
    ("hospital", "clinic", 0.75),
    # Nature
    ("river", "stream", 0.82),
    ("mountain", "hill", 0.78),
    ("forest", "jungle", 0.72),
    ("ocean", "sea", 0.90),
    ("desert", "dune", 0.65),
    ("rain", "snow", 0.72),
    ("sun", "moon", 0.60),
    ("fire", "water", 0.20),
    ("wind", "storm", 0.65),
    ("rock", "stone", 0.95),
    # Tech
    ("phone", "tablet", 0.78),
    ("laptop", "desktop", 0.80),
    ("keyboard", "mouse", 0.75),
    ("server", "cloud", 0.70),
    ("code", "script", 0.88),
    # Abstract / Concepts
    ("love", "hate", 0.15),
    ("war", "peace", 0.10),
    ("day", "night", 0.20),
    ("past", "future", 0.25),
    ("truth", "lie", 0.10),
    ("light", "shadow", 0.30),
    ("hope", "fear", 0.20),
    ("joy", "sorrow", 0.15),
    ("begin", "end", 0.20),
    ("give", "take", 0.20),
    # Sports
    ("football", "basketball", 0.65),
    ("tennis", "badminton", 0.78),
    ("swimming", "running", 0.55),
    ("boxing", "wrestling", 0.68),
    ("golf", "cricket", 0.45),
    # Colors
    ("red", "blue", 0.50),
    ("black", "white", 0.20),
    ("gold", "silver", 0.72),
    ("green", "brown", 0.40),
    # Body
    ("hand", "foot", 0.65),
    ("eye", "ear", 0.60),
    ("heart", "brain", 0.55),
    ("bone", "muscle", 0.65),
    # Time
    ("second", "minute", 0.85),
    ("hour", "day", 0.75),
    ("week", "month", 0.78),
    ("morning", "evening", 0.55),
    ("summer", "winter", 0.40),
    # Cross domain - clear mismatches
    ("cat", "server", 0.02),
    ("mountain", "keyboard", 0.02),
    ("coffee", "knight", 0.03),
    ("rain", "bicycle", 0.05),
    ("love", "truck", 0.01),
    ("hospital", "eagle", 0.03),
    ("sugar", "war", 0.02),
    ("ocean", "laptop", 0.03),
]


class MethodTester:
    def __init__(self, methods):
        self.methods = methods
        self.word_pairs = word_pairs_with_scores
        self._warmup()

    def _warmup(self):
        print("Warming up methods...")
        for method in self.methods:
            try:
                method("test", "test")
            except Exception:
                pass
        print("Warmup done.\n")

    def test_methods_time(self):
        results = {}
        for method in self.methods:
            start_time = time.time()
            for word1, word2, _ in self.word_pairs:
                method(word1, word2)
            end_time = time.time()
            results[method.__name__] = end_time - start_time
        return results

    def test_methods_memory(self):
        results = {}
        for method in self.methods:
            gc.collect()
            tracemalloc.start()

            for word1, word2, _ in self.word_pairs:
                method(word1, word2)

            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            results[method.__name__] = {
                "current_mb": round(current / 1024 / 1024, 4),
                "peak_mb": round(peak / 1024 / 1024, 4),
            }
        return results

    def test_methods_similarity_word(self):
        results = {}
        for method in self.methods:
            similarities = []
            total_error = 0.0
            for word1, word2, expected in self.word_pairs:
                similarity = method(word1, word2)
                error = abs(similarity - expected)
                total_error += error
                similarities.append(
                    f"{word1} - {word2}: predicted={similarity:.4f} | expected={expected:.4f} | error={error:.4f}"
                )
            avg_error = total_error / len(self.word_pairs)
            results[method.__name__] = {
                "pairs": similarities,
                "avg_error": round(avg_error, 4),
                "avg_accuracy": round(1 - avg_error, 4),
            }
        return results

    def test_methods_similarity_sentence(self):
        results = {}
        scored_pairs = (
            [(s1, s2, 0.85) for s1, s2 in strong_matches]
            + [(s1, s2, 0.55) for s1, s2 in partial_matches]
            + [(s1, s2, 0.08) for s1, s2 in mismatches]
        )
        for method in self.methods:
            similarities = []
            total_error = 0.0
            for sent1, sent2, expected in scored_pairs:
                similarity = method(sent1, sent2)
                error = abs(similarity - expected)
                total_error += error
                similarities.append(
                    f"{sent1} | {sent2}: predicted={similarity:.4f} | expected={expected:.4f} | error={error:.4f}"
                )
            avg_error = total_error / len(scored_pairs)
            results[method.__name__] = {
                "pairs": similarities,
                "avg_error": round(avg_error, 4),
                "avg_accuracy": round(1 - avg_error, 4),
            }
        return results

    def run_tests(self):
        print("Testing time...")
        time_results = self.test_methods_time()

        print("Testing memory...")
        memory_results = self.test_methods_memory()

        print("Testing word similarity...")
        similarity_results = self.test_methods_similarity_word()

        print("Testing sentence similarity...")
        sentence_results = self.test_methods_similarity_sentence()

        test_results = {}
        for method in self.methods:
            name = method.__name__
            test_results[name] = {
                "time": time_results[name],
                "mem_current_mb": memory_results[name]["current_mb"],
                "mem_peak_mb": memory_results[name]["peak_mb"],
                "similarity_accuracy_word": similarity_results[name]["avg_accuracy"],
                "similarity_accuracy_sentence": sentence_results[name]["avg_accuracy"],
            }

        sorted_by_time = sorted(test_results, key=lambda n: test_results[n]["time"])
        sorted_by_mem = sorted(
            test_results, key=lambda n: test_results[n]["mem_peak_mb"]
        )
        sorted_by_word = sorted(
            test_results,
            key=lambda n: test_results[n]["similarity_accuracy_word"],
            reverse=True,
        )
        sorted_by_sentence = sorted(
            test_results,
            key=lambda n: test_results[n]["similarity_accuracy_sentence"],
            reverse=True,
        )

        for name in test_results:
            test_results[name]["rank_time"] = sorted_by_time.index(name) + 1
            test_results[name]["rank_mem"] = sorted_by_mem.index(name) + 1
            test_results[name]["rank_word"] = sorted_by_word.index(name) + 1
            test_results[name]["rank_sentence"] = sorted_by_sentence.index(name) + 1
            test_results[name]["rank_overall"] = (
                test_results[name]["rank_time"]
                + test_results[name]["rank_mem"]
                + test_results[name]["rank_word"]
                + test_results[name]["rank_sentence"]
            ) / 4

        test_results = dict(
            sorted(test_results.items(), key=lambda item: item[1]["rank_overall"])
        )

        print("Done.\n")
        return test_results
