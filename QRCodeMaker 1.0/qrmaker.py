import qrcode # type: ignore
import qrcode_terminal # type: ignore
import os
import sys
from pathlib import Path
from datetime import datetime

def get_save_path(filename):
    """get the path to GeneratedQR folder"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the full path to the GeneratedQR folder
    save_dir = os.path.join(script_dir, "GeneratedQR")
    
    # Create the folder if it doesn't exist
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    
    # Return the full path including the filename
    return os.path.join(save_dir, filename)

def generate_terminalQR(data):
    """Generate and display QR code in terminal"""
    try:
        print("\n")
        print("YOUR QR CODE:")
        print("="*50 + "\n")
        
        # Generate and display QR code in terminal
        qrcode_terminal.draw(data)
        
    except Exception as e:
        print(f"Error generating QR or invalid input: {e}")
        generate_imageQR(data)

def generate_imageQR(data):
    """Save generated QR as image in GeneratedQR folder"""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Create filename with timestamp to avoid overwriting
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Clean the data for filename
        filename = f"qr_{timestamp}.png"
        
        # Save to GeneratedQR folder
        full_path = get_save_path(filename)
        img.save(full_path)
        
        print(f"\n✅ QR Code saved as: {filename}")
        print(f"📁 Location: {full_path}")
        
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main program flow"""
    print("\n" + "="*50)
    print("🎯 QR CODE GENERATOR")
    
    # Show where files will be saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    save_dir = os.path.join(script_dir, "GeneratedQR")
    print(f"📁 Files will be saved to: {save_dir}")
    print("="*50)
    
    while True:
        choice = input("\nEnter link (x to exit): ").strip()
        
        if choice.lower() == "x":
            print("\n👋 Goodbye!")
            break
        elif not choice:
            print("❌ No input provided. Please try again.")
            continue
        else:            
            data = choice.encode('utf-8')
            print(f"\n🔨 Generating QR Code for: {choice}")
            print("-"*50)

            while True:
                # Ask for display preference
                print("\nDisplay options:")
                print("1. Terminal QR Code")
                print("2. Save as Image")
                print("3. Both formats")
                
                display_choice = input("\nSelect option (1-3): ").strip()
                
                if display_choice == "1":
                    generate_terminalQR(data)
                    break
                elif display_choice == "2":
                    generate_imageQR(data)
                    break
                elif display_choice == "3":
                    generate_terminalQR(data)
                    generate_imageQR(data)
                    break
                else:
                    print("❌ Invalid option. Please select 1, 2, or 3.")
            
            print("\n" + "-"*50)
            print("✅ Done!")
            print("-"*50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)