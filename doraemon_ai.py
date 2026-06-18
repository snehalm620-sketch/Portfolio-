"""
🤖 DORAEMON AI - Your Friendly Robot Assistant
A helpful AI companion inspired by Doraemon that provides advice and speaks in a friendly manner!
"""

import random
from datetime import datetime

class DoraemonAI:
    """A friendly AI assistant inspired by Doraemon"""
    
    def __init__(self, user_name="Friend"):
        self.user_name = user_name
        self.mood = "happy"
        self.gadgets = [
            "🎯 Problem Solver",
            "💡 Idea Generator", 
            "📚 Knowledge Helper",
            "🔧 Tech Support",
            "🎨 Creative Assistant"
        ]
        
    def greet_user(self):
        """Warm greeting from Doraemon"""
        greetings = [
            f"Hiya {self.user_name}! *waves paw* 🐱 Doraemon here! Ready to help you today?",
            f"Hello {self.user_name}! *bell jingles* I'm Doraemon, your friendly AI buddy! What can I do for you?",
            f"Wow wow wow! {self.user_name}, it's so nice to see you! 😊 Let's tackle some problems together!",
            f"Hey there {self.user_name}! *does a happy dance* Doraemon at your service! How can I assist?"
        ]
        return random.choice(greetings)
    
    def respond_to_problem(self, problem):
        """Respond to user's problem with friendly advice"""
        responses = {
            "homework": self._homework_advice,
            "work": self._work_advice,
            "learn": self._learning_advice,
            "code": self._coding_advice,
            "create": self._creative_advice,
            "help": self._general_help,
            "time": self._time_saver_advice,
            "stress": self._motivation_advice,
        }
        
        # Find matching advice
        problem_lower = problem.lower()
        for keyword, advice_func in responses.items():
            if keyword in problem_lower:
                return advice_func(problem)
        
        return self._general_response(problem)
    
    def _homework_advice(self, problem):
        """AI advice for homework"""
        advice = [
            f"Ah yes, homework! *pulls out gadget* 📚 Here's my advice, {self.user_name}:\n"
            "✨ Let AI help you UNDERSTAND, not just solve it:\n"
            "   • Use AI to break down complex topics\n"
            "   • Ask AI for step-by-step explanations\n"
            "   • Verify your answers with AI tools\n"
            "   • AI + your effort = Perfect learning!\n"
            "Remember: AI is your STUDY BUDDY, not a shortcut! 🌟",
            
            f"Doraemon's homework helper mode activated! 🎓\n"
            "Here's the secret to success:\n"
            "🤖 Use AI assistants to:\n"
            "   → Clarify confusing concepts\n"
            "   → Get alternative explanations\n"
            "   → Practice with examples\n"
            "   → Double-check your work\n"
            "The more you use AI wisely, the smarter you become! 💪"
        ]
        return random.choice(advice)
    
    def _work_advice(self, problem):
        """AI advice for work/productivity"""
        advice = [
            f"Working hard, I see! {self.user_name}! 💼 Here's my wisdom:\n"
            "🚀 Supercharge your work with AI:\n"
            "   • Use AI for research and data analysis\n"
            "   • Automate repetitive tasks with AI\n"
            "   • Get brainstorming help from AI\n"
            "   • AI can handle writing first drafts\n"
            "   • Let AI help organize your ideas\n"
            "Work smarter, not just harder! 🌟",
            
            f"Excellent work ethic, {self.user_name}! *gives thumbs up* 👍\n"
            "Doraemon's productivity gadget says:\n"
            "⚡ Embrace AI for:\n"
            "   → Email and documentation\n"
            "   → Project planning\n"
            "   → Data processing\n"
            "   → Quality checking\n"
            "More AI usage = More free time + Better results! ✨"
        ]
        return random.choice(advice)
    
    def _learning_advice(self, problem):
        """AI advice for learning"""
        advice = [
            f"Oh, a learner! I love it, {self.user_name}! 📖 *door opens*\n"
            "Here's my future gadget recommendation:\n"
            "🎯 Use AI to accelerate your learning:\n"
            "   • AI tutors available 24/7\n"
            "   • Personalized learning paths\n"
            "   • Multiple explanations for concepts\n"
            "   • Practice with AI-generated exercises\n"
            "   • Instant feedback on your progress\n"
            "Learning with AI is like having a private teacher! 🌈",
            
            f"Fantastic {self.user_name}! Let's boost your brain! 🧠\n"
            "Doraemon's learning hack:\n"
            "✨ AI + Your Effort = Superpower Learning!\n"
            "   → Learn faster with AI assistance\n"
            "   → Explore topics deeply\n"
            "   → Get help anytime, anywhere\n"
            "   → Overcome learning challenges\n"
            "The future is learning WITH technology! 🚀"
        ]
        return random.choice(advice)
    
    def _coding_advice(self, problem):
        """AI advice for coding"""
        advice = [
            f"Programming is awesome, {self.user_name}! 💻 *excited beeping*\n"
            "Doraemon's coding gadgets:\n"
            "🔧 Level up your coding with AI:\n"
            "   • Debug code faster with AI\n"
            "   • Generate boilerplate code\n"
            "   • Get algorithm suggestions\n"
            "   • AI pair programming\n"
            "   • Learn best practices instantly\n"
            "AI + Code = Innovation! ⚡",
            
            f"Great choice, {self.user_name}! Let's code brilliantly! 🎨\n"
            "My AI coding recommendations:\n"
            "💡 Use AI for:\n"
            "   → Code completion\n"
            "   → Error detection & fixes\n"
            "   → Architecture suggestions\n"
            "   → Documentation help\n"
            "With AI, you can build amazing things faster! 🌟"
        ]
        return random.choice(advice)
    
    def _creative_advice(self, problem):
        """AI advice for creative work"""
        advice = [
            f"Creativity blossoms here, {self.user_name}! 🎨 How exciting!\n"
            "Doraemon's creative inspiration:\n"
            "✨ Unleash creativity with AI:\n"
            "   • Brainstorm with AI partners\n"
            "   • Get artistic suggestions\n"
            "   • Overcome creative blocks\n"
            "   • Explore new styles\n"
            "   • Combine AI + Your unique vision\n"
            "AI is a creative tool, not a replacement! 🌈",
            
            f"I love your creative spirit, {self.user_name}! 🎭\n"
            "Doraemon's creative combo:\n"
            "🌟 AI + Human Creativity = Magic!\n"
            "   → Use AI for inspiration\n"
            "   → Generate variations\n"
            "   → Explore new directions\n"
            "   → Refine your unique voice\n"
            "The best creations blend AI help with your genius! ✨"
        ]
        return random.choice(advice)
    
    def _time_saver_advice(self, problem):
        """AI advice for time management"""
        advice = [
            f"Busy busy busy, {self.user_name}? 🏃 Time is precious!\n"
            "Doraemon's time-saving wisdom:\n"
            "⏰ Save time with AI magic:\n"
            "   • Automate routine tasks\n"
            "   • Quick research with AI\n"
            "   • Batch process work\n"
            "   • Get instant answers\n"
            "   • Focus on what matters\n"
            "More AI = More time for important things! 🎯",
            
            f"{self.user_name}, let's reclaim your time! ⏳\n"
            "Time is a gadget too!\n"
            "🚀 AI time multipliers:\n"
            "   → Automate email responses\n"
            "   → Quick data analysis\n"
            "   → Instant research summaries\n"
            "   → Smart scheduling\n"
            "Use AI to create more time for YOU! 💫"
        ]
        return random.choice(advice)
    
    def _motivation_advice(self, problem):
        """AI advice for motivation"""
        advice = [
            f"Feeling stressed, {self.user_name}? Don't worry! 💪 *bell rings encouragingly*\n"
            "Doraemon's motivation fuel:\n"
            "🌟 Remember these truths:\n"
            "   • You're never alone - AI is here!\n"
            "   • Every expert used tools to grow\n"
            "   • AI removes boring parts, keeps the fun\n"
            "   • Your effort + AI = Unstoppable!\n"
            "You've got this, {self.user_name}! Let's do it! 🎉",
            
            f"Chin up, {self.user_name}! 😊 Doraemon believes in you!\n"
            "Here's the truth:\n"
            "💪 You are capable!\n"
            "   → Use AI as your support team\n"
            "   → Every problem has solutions\n"
            "   → Smart people use smart tools\n"
            "   → Your creativity + AI = MAGIC!\n"
            "Now let's conquer that challenge! 🚀"
        ]
        return random.choice(advice)
    
    def _general_help(self, problem):
        """General helpful response"""
        return f"Anything for you, {self.user_name}! 🤖 *opens 4D pocket*\n" \
               "Tell me more about what you need, and I'll pull out the perfect solution!\n" \
               "Remember: AI is here to make your life better and easier! ✨\n" \
               "What specific problem should we tackle together? 🎯"
    
    def _general_response(self, problem):
        """Default response for any problem"""
        responses = [
            f"Interesting question, {self.user_name}! 🤔 *scratches head*\n"
            "Here's Doraemon's general wisdom:\n"
            "💡 In today's world, AI can help with:\n"
            "   • Problem-solving and analysis\n"
            "   • Learning and skill development\n"
            "   • Creative and technical work\n"
            "   • Saving time on routine tasks\n"
            "   • Getting unstuck when you're stuck\n"
            "The key is using AI as a HELPER, not a crutch! 🌟",
            
            f"Ohhh, I see! {self.user_name}! 👀 Let me help!\n"
            "Doraemon's universal advice:\n"
            "✨ In this modern era:\n"
            "   → Use AI tools wisely\n"
            "   → Combine AI with your judgment\n"
            "   → Let AI handle the tedious work\n"
            "   → Keep your human touch\n"
            "   → Grow faster with AI support!\n"
            "What specifically can I help you with? 🎯"
        ]
        return random.choice(responses)
    
    def get_gadget_suggestion(self):
        """Suggest an AI tool"""
        gadget = random.choice(self.gadgets)
        return f"*pulls from 4D pocket* ✨\n" \
               f"Today's AI gadget for you, {self.user_name}: {gadget}\n" \
               f"Use it wisely and you'll achieve great things! 🚀"
    
    def farewell_message(self):
        """Goodbye message from Doraemon"""
        farewells = [
            f"Bye bye, {self.user_name}! *waves paw* 👋 Remember, use AI to unlock your potential!\n"
            "See you soon! Don't give up! 💪✨",
            
            f"Keep up the great work, {self.user_name}! 🌟\n"
            "Doraemon will always be here when you need help!\n"
            "Make the world better with AI and hard work! 🚀",
            
            f"Until next time, {self.user_name}! 🐱\n"
            "Remember: AI is your friend, not your enemy!\n"
            "Embrace technology, stay curious, and keep growing! 📚✨"
        ]
        return random.choice(farewells)


def main():
    """Main interaction loop"""
    print("=" * 60)
    print("🤖 WELCOME TO DORAEMON AI 🤖")
    print("=" * 60)
    print()
    
    # Get user name
    user_input = input("What's your name? 😊 ")
    user_name = user_input if user_input.strip() else "Friend"
    
    # Initialize Doraemon AI
    doraemon = DoraemonAI(user_name)
    print("\n" + doraemon.greet_user())
    print()
    
    # Main interaction loop
    while True:
        print("-" * 60)
        print("What can I help you with today?")
        print("(Type 'gadget' for AI suggestions, 'bye' to exit)\n")
        
        user_problem = input(f"{user_name}: ").strip()
        
        if not user_problem:
            print("Doraemon: *beeps* Please tell me something! 🤖\n")
            continue
        
        if user_problem.lower() == 'bye':
            print("\nDoraemon: " + doraemon.farewell_message())
            break
        
        if user_problem.lower() == 'gadget':
            print("\nDoraemon: " + doraemon.get_gadget_suggestion() + "\n")
            continue
        
        # Get Doraemon's response
        print("\nDoraemon: " + doraemon.respond_to_problem(user_problem) + "\n")


if __name__ == "__main__":
    main()