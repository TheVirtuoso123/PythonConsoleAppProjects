import os
import sys
import tempfile
from pathlib import Path
from datetime import datetime
from gtts import gTTS # type: ignore
import pygame # type: ignore

class TextToSpeech:
    def __init__(self):
        """Initialize the TTS system"""
        self.languages = {
            '1': {'code': 'en', 'name': 'English (US)'},
            '2': {'code': 'en-uk', 'name': 'English (UK)'},
            '3': {'code': 'en-au', 'name': 'English (Australia)'},
            '4': {'code': 'en-ca', 'name': 'English (Canada)'},
            '5': {'code': 'es', 'name': 'Spanish'},
            '6': {'code': 'fr', 'name': 'French'},
            '7': {'code': 'de', 'name': 'German'},
            '8': {'code': 'it', 'name': 'Italian'},
            '9': {'code': 'pt', 'name': 'Portuguese'},
            '10': {'code': 'ru', 'name': 'Russian'},
            '11': {'code': 'ja', 'name': 'Japanese'},
            '12': {'code': 'ko', 'name': 'Korean'},
            '13': {'code': 'zh-CN', 'name': 'Chinese (Simplified)'},
            '14': {'code': 'hi', 'name': 'Hindi'},
            '15': {'code': 'ar', 'name': 'Arabic'},
            '16': {'code': 'nl', 'name': 'Dutch'},
            '17': {'code': 'pl', 'name': 'Polish'},
            '18': {'code': 'tr', 'name': 'Turkish'},
            '19': {'code': 'vi', 'name': 'Vietnamese'},
            '20': {'code': 'id', 'name': 'Indonesian'}
        }
        
        # Default language
        self.current_lang = 'en'
        self.current_lang_name = 'English (US)'
        self.slow_speed = False
        
        # Initialize pygame mixer
        try:
            pygame.mixer.init()
            print("✅ Audio system initialized!")
        except Exception as e:
            print(f"⚠️  Could not initialize audio: {e}")
            print("💡 Installing pygame might help: pip install pygame")

    def get_save_path(self, filename):
        """get the path to GeneratedSpeech folder"""
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
        # Create the full path to the GeneratedSpeech folder
        save_dir = os.path.join(script_dir, "GeneratedSpeech")
    
        # Create the folder if it doesn't exist
        Path(save_dir).mkdir(parents=True, exist_ok=True)
    
        # Return the full path including the filename
        return os.path.join(save_dir, filename)
    
    def list_languages(self):
        """List available languages"""
        print("\n" + "="*50)
        print("🌐 AVAILABLE LANGUAGES:")
        print("="*50)
        
        # Display in columns for better readability
        items = list(self.languages.items())
        for i in range(0, len(items), 3):
            line = ""
            for j in range(3):
                if i + j < len(items):
                    key, value = items[i + j]
                    line += f"  {key}. {value['name']:<20}"
            print(line)
        print("="*50)
    
    def change_language(self):
        """Interactive language change menu"""
        self.list_languages()
        
        try:
            choice = input(f"\n👉 Select language (1-{len(self.languages)}), or 0 to cancel: ").strip()
            
            if choice == "0":
                print("❌ Language change cancelled")
                return
            
            if choice in self.languages:
                self.current_lang = self.languages[choice]['code']
                self.current_lang_name = self.languages[choice]['name']
                print(f"✅ Language changed to: {self.current_lang_name}")
            else:
                print(f"❌ Invalid choice. Please select 1-{len(self.languages)}")
                
        except Exception as e:
            print(f"❌ Error changing language: {e}")
    
    def toggle_speed(self):
        """Toggle between normal and slow speech"""
        self.slow_speed = not self.slow_speed
        speed_text = "SLOW" if self.slow_speed else "NORMAL"
        print(f"✅ Speech speed set to: {speed_text}")
    
    def save_to_file(self, text, filename):
        """Save text as audio file"""
        try:
            if not text.strip():
                print("❌ No text to save!")
                return
            
            # Make sure filename has extension
            if not filename.endswith('.mp3'):
                filename += '.mp3'
            
            print(f"\n💾 Saving: {text}")
            print(f"🌐 Language: {self.current_lang_name}")
            print(f"⚡ Speed: {'Slow' if self.slow_speed else 'Normal'}")
            
            # Create gTTS object
            tts = gTTS(
                text=text, 
                lang=self.current_lang, 
                slow=self.slow_speed
            )
            
            # Save to file
            full_path = self.get_save_path(filename)
            tts.save(full_path)
            
            # Get absolute path
            abs_path = os.path.abspath(full_path)
            print(f"✅ Speech saved to: {abs_path}")
            print(f"📁 File size: {os.path.getsize(abs_path)} bytes")
            
        except Exception as e:
            print(f"❌ Error saving speech: {e}")
    
    def get_current_settings(self):
        """Get current settings as string"""
        return f"Language: {self.current_lang_name}, Speed: {'Slow' if self.slow_speed else 'Normal'}"

def main():
    """Main program flow"""
    print("\n" + "="*55)
    print("🗣️  TEXT-TO-SPEECH CONVERTER (gTTS)")
    print("="*55 + "\n")
    
    # Initialize TTS, ease of prototype usage
    tts = TextToSpeech()
    
    while True:
        print("\n" + "="*55)
        print(f"📌 MENU  [📊 Current Settings: {tts.get_current_settings()}]")
        print("  1. Save Speech to File")
        print("  2. Change Language")
        print("  3. Toggle Speed (Normal/Slow)")
        print("  4. Exit")
        print("="*55)
        
        choice = input("\n👉 Select option (1-4): ").strip()
        
        if choice == "4":
            print("\n👋 Goodbye! Thanks for using TTS Converter!")
            break
        
        elif choice == "1":
            text = input("\n📝 Enter text to save: ").strip()
            if text:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                default_filename = f"speech_{timestamp}.mp3"
                
                filename = input(f"📁 Enter filename (default: {default_filename}): ").strip()
                if not filename:
                    filename = default_filename
                
                tts.save_to_file(text, filename)
        
        elif choice == "2":
            tts.change_language()
            print(f"\n📊 Current Settings:")
            print(f"   {tts.get_current_settings()}")
        
        elif choice == "3":
            tts.toggle_speed()
            print(f"\n📊 Current Settings:")
            print(f"   {tts.get_current_settings()}")
        
        else:
            print("❌ Invalid option. Please select 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        sys.exit(1)