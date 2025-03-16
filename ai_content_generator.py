import openai
import random
import json
import os

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

class ContentGenerator:
    def __init__(self, model="text-davinci-003"):
        self.model = model

    def generate_content(self, prompt, max_tokens=100):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()

    def generate_blog_post(self, title, subject, keywords):
        prompt = f"Write a blog post titled '{title}' about {subject}, using the keywords {keywords}."
        content = self.generate_content(prompt, max_tokens=500)
        return content

    def generate_social_media_post(self, topic):
        prompt = f"Create a catchy social media post about {topic}."
        content = self.generate_content(prompt, max_tokens=280)
        return content

    def generate_video_script(self, theme):
        prompt = f"Write a video script for a YouTube video on the theme: {theme}."
        content = self.generate_content(prompt, max_tokens=600)
        return content

def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    generator = ContentGenerator()
    
    # Example usage for blog post generation
    blog_title = "The Future of Artificial Intelligence"
    blog_subject = "exploring the trends and advancements in AI"
    blog_keywords = "AI, future, technology, trends"
    blog_post = generator.generate_blog_post(blog_title, blog_subject, blog_keywords)
    print("Generated Blog Post:\n", blog_post)
    save_to_file("blog_post.txt", blog_post)
    
    # Example usage for social media post generation
    social_topic = "AI in Everyday Life"
    social_post = generator.generate_social_media_post(social_topic)
    print("\nGenerated Social Media Post:\n", social_post)
    save_to_file("social_media_post.txt", social_post)
    
    # Example usage for video script generation
    video_theme = "Exploring AI Technologies"
    video_script = generator.generate_video_script(video_theme)
    print("\nGenerated Video Script:\n", video_script)
    save_to_file("video_script.txt", video_script)

if __name__ == "__main__":
    main()

# Additional features to extend the capability of the content generator

class AdvancedContentGenerator(ContentGenerator):
    def generate_email_campaign(self, subject_line, email_body):
        prompt = f"Create an engaging email campaign with subject line '{subject_line}' and body '{email_body}'."
        content = self.generate_content(prompt, max_tokens=300)
        return content

    def generate_product_descriptions(self, product_name, features):
        prompt = f"Write a product description for {product_name}, highlighting the following features: {features}."
        content = self.generate_content(prompt, max_tokens=250)
        return content

def test_advanced_generator():
    advanced_gen = AdvancedContentGenerator()

    # Test email campaign
    email_subject = "Unlock the Future of AI!"
    email_body = "Discover how our new AI tools can transform your business."
    email_campaign = advanced_gen.generate_email_campaign(email_subject, email_body)
    print("\nGenerated Email Campaign:\n", email_campaign)
    save_to_file("email_campaign.txt", email_campaign)

    # Test product description
    product_name = "Smart AI Assistant"
    product_features = "voice recognition, task automation, 24/7 availability"
    product_description = advanced_gen.generate_product_descriptions(product_name, product_features)
    print("\nGenerated Product Description:\n", product_description)
    save_to_file("product_description.txt", product_description)

if __name__ == "__main__":
    test_advanced_generator()

# Adding user interaction for a more dynamic use case

def interactive_content_generation():
    print("\nWelcome to the AI Content Generator!")
    while True:
        print("Choose the type of content to generate:")
        print("1. Blog Post")
        print("2. Social Media Post")
        print("3. Video Script")
        print("4. Email Campaign")
        print("5. Product Description")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter blog post title: ")
            subject = input("Enter blog post subject: ")
            keywords = input("Enter keywords (comma-separated): ")
            generated_content = generator.generate_blog_post(title, subject, keywords)
            print("\nGenerated Blog Post:\n", generated_content)
        elif choice == '2':
            topic = input("Enter topic for social media post: ")
            generated_content = generator.generate_social_media_post(topic)
            print("\nGenerated Social Media Post:\n", generated_content)
        elif choice == '3':
            theme = input("Enter theme for video script: ")
            generated_content = generator.generate_video_script(theme)
            print("\nGenerated Video Script:\n", generated_content)
        elif choice == '4':
            email_subject = input("Enter email subject: ")
            email_body = input("Enter email body: ")
            generated_content = advanced_gen.generate_email_campaign(email_subject, email_body)
            print("\nGenerated Email Campaign:\n", generated_content)
        elif choice == '5':
            product_name = input("Enter product name: ")
            features = input("Enter features (comma-separated): ")
            generated_content = advanced_gen.generate_product_descriptions(product_name, features)
            print("\nGenerated Product Description:\n", generated_content)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    interactive_content_generation()