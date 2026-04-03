from agents.orchestrator_agent import build_menu, suggest_dishes

cuisine = input("Enter cuisine: ")

# Step 1
dishes = suggest_dishes(cuisine)

print("Suggested dishes:", dishes)

# Step 2
selected = dishes[:10]

# Step 3
pdf = build_menu(cuisine, selected)

print("Menu created:", pdf)