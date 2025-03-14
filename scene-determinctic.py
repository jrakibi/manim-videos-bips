from manim import *
import random

# Sample BIP-39 mnemonic words (we'll randomly select 12 from these)
BIP39_WORDS = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
    "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
    "acoustic", "acquire", "across", "act", "action", "actor", "actual", "adapt",
    "add", "addict", "address", "adjust", "admit", "adult", "advance", "advice",
    "aerobic", "affair", "afford", "afraid", "again", "age", "agent", "agree",
    "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also",
    "alter", "always", "amateur", "amazing", "among", "amount", "amused", "analyst"
]

class BitcoinWalletAnimation(MovingCameraScene):
    def construct(self):
        # Main animation that runs all scenes sequentially
        self.scene1_mnemonic_intro()
        self.scene2_wallet_types()
        self.scene3_non_deterministic_wallets()
        # self.scene4_deterministic_wallets()
        # self.scene5_mnemonic_generation()
        # Add more scenes as needed: self.scene5_...(), etc.
    
    #######################
    # SCENE 1: Mnemonic Introduction
    #######################
    def scene1_mnemonic_intro(self):
        # Scene 1: Introducing Mnemonic Code Words (BIP-39)
        self.ask_wallet_security_question()
    
    def ask_wallet_security_question(self):
        # Create the question text with all words in the same color, split into two rows
        question_line1 = Text("Have you ever wondered how Bitcoin wallets", font_size=36)
        question_line2 = Text("keep your keys safe & organized?", font_size=36)
        
        # Create a VGroup to center both lines together
        question_group = VGroup(question_line1, question_line2)
        question_group.arrange(DOWN, buff=0.5)
        
        # Position the text group in the center of the screen
        question_group.move_to(ORIGIN)
        
        # Animate the question appearance
        self.play(Write(question_line1), run_time=1.5)
        self.play(Write(question_line2), run_time=1.5)
        
        # Wait for the viewer to read
        self.wait(3)
        
        # Fade out the question to transition to the next part
        self.play(FadeOut(question_line1), FadeOut(question_line2))

    #######################
    # SCENE 2: Wallet Types
    #######################
    def scene2_wallet_types(self):
        # Scene 2: Types of Bitcoin Wallets
        self.introduce_wallet_types()
    
    def introduce_wallet_types(self):
        # Main title - centered and with proper size and margin from top
        title = Text("Bitcoin has 2 types of wallets", font_size=42)
        title.move_to(ORIGIN)
        
        self.play(FadeIn(title))
        self.wait(1)
        
        # Move title to top with proper margin
        self.play(title.animate.to_edge(UP, buff=0.6))
        
        # Create tree diagram - moved up to be closer to title
        tree_center = Dot(color=YELLOW)
        tree_center.move_to(UP * 1.5)
        
        # Calculate optimal positions for branches to ensure symmetry
        # Increased horizontal spread for better separation
        left_end = LEFT * 3.0 + DOWN * 0.2
        right_end = RIGHT * 3.0 + DOWN * 0.2
        
        # Create branches with adjusted positions
        left_branch = Arrow(
            start=tree_center.get_center(),
            end=left_end,
            buff=0.1,
            color=BLUE
        )
        
        right_branch = Arrow(
            start=tree_center.get_center(),
            end=right_end,
            buff=0.1,
            color=RED
        )
        
        # Create wallet type labels with appropriate font size
        deterministic = Text("Deterministic Wallets", font_size=28, color=BLUE)
        non_deterministic = Text("Non-Deterministic Wallets", font_size=28, color=RED)
        
        # Position labels directly below arrow endpoints
        deterministic.next_to(left_branch.get_end(), DOWN, buff=0.2)
        non_deterministic.next_to(right_branch.get_end(), DOWN, buff=0.2)
        
        # Ensure labels are horizontally centered with their respective arrows
        deterministic.move_to([left_end[0], deterministic.get_center()[1], 0])
        non_deterministic.move_to([right_end[0], non_deterministic.get_center()[1], 0])
        
        # Animate tree diagram
        self.play(GrowFromCenter(tree_center))
        self.play(
            GrowArrow(left_branch),
            GrowArrow(right_branch),
            run_time=1.5
        )
        self.play(
            Write(deterministic),
            Write(non_deterministic),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Create wallet icons with appropriate scale
        deterministic_icon = self.create_deterministic_wallet_icon()
        non_deterministic_icon = self.create_non_deterministic_wallet_icon()
        
        # Scale icons to fit properly
        deterministic_icon.scale(0.85)
        non_deterministic_icon.scale(0.85)
        
        # Position icons with proper spacing
        deterministic_icon.next_to(deterministic, DOWN, buff=0.4)
        non_deterministic_icon.next_to(non_deterministic, DOWN, buff=0.4)
        
        # Ensure icons are horizontally centered with their labels
        deterministic_icon.move_to([deterministic.get_center()[0], deterministic_icon.get_center()[1], 0])
        non_deterministic_icon.move_to([non_deterministic.get_center()[0], non_deterministic_icon.get_center()[1], 0])
        
        # Animate wallet icons
        self.play(
            FadeIn(deterministic_icon),
            FadeIn(non_deterministic_icon),
            run_time=1.5
        )
        
        self.wait(1)
        
        # Add descriptions with appropriate font size
        det_desc = Text("One seed generates multiple keys", font_size=22, color=BLUE_C)
        non_det_desc = Text("Separate, unlinked keys", font_size=22, color=RED_C)
        
        # First position them under their respective icons
        det_desc.next_to(deterministic_icon, DOWN, buff=0.3)
        non_det_desc.next_to(non_deterministic_icon, DOWN, buff=0.3)
        
        # Ensure descriptions are horizontally centered with their icons
        det_desc.move_to([deterministic_icon.get_center()[0], det_desc.get_center()[1], 0])
        non_det_desc.move_to([non_deterministic_icon.get_center()[0], non_det_desc.get_center()[1], 0])
        
        # Get the lowest y-position to align both texts at the same height
        lowest_y = min(det_desc.get_center()[1], non_det_desc.get_center()[1])
        
        # Move both descriptions to the same y-position
        det_desc.move_to([det_desc.get_center()[0], lowest_y, 0])
        non_det_desc.move_to([non_det_desc.get_center()[0], lowest_y, 0])
        
        # Check if descriptions go off-screen and adjust camera if needed
        screen_bottom = -3.5
        if det_desc.get_bottom()[1] < screen_bottom or non_det_desc.get_bottom()[1] < screen_bottom:
            # Zoom out slightly to accommodate all elements
            self.play(
                self.camera.frame.animate.scale(1.2).move_to(DOWN * 0.5),
                run_time=1.5,
                rate_func=smooth
            )
        
        # Now write the descriptions
        self.play(
            Write(det_desc),
            Write(non_det_desc),
            run_time=1.5
        )
        
        # Group all elements for reference
        all_elements = VGroup(
            title, tree_center, left_branch, right_branch,
            deterministic, non_deterministic,
            deterministic_icon, non_deterministic_icon,
            det_desc, non_det_desc
        )
        
        # Instead of fading out everything, we'll keep the non-deterministic side
        # and fade out only the deterministic side for a smooth transition
        deterministic_side = VGroup(
            left_branch, right_branch, deterministic, deterministic_icon, det_desc, non_deterministic_icon
        )
        
        non_deterministic_side = VGroup(
            right_branch, non_deterministic, non_deterministic_icon, non_det_desc
        )
        
        center_elements = VGroup(title, tree_center)
        
        # Fade out deterministic side and center elements
        self.play(
            FadeOut(deterministic_side),
            FadeOut(center_elements),
            run_time=1
        )
        
        # Move non-deterministic elements to prepare for scene 3
        self.play(
            non_deterministic.animate.scale(1.2).move_to(UP * 3),
            # non_deterministic_icon.animate.scale(0.8).move_to(UP * 1),
            FadeOut(non_det_desc),
            run_time=1.5
        )
        
        # Reset camera frame if it was zoomed
        self.play(
            self.camera.frame.animate.scale(1/1.2).move_to(ORIGIN),
            run_time=1,
            rate_func=smooth
        )
        
        # Save these elements to be used in the next scene
        self.non_deterministic_title = non_deterministic

    #######################
    # SCENE 3: Non-Deterministic Wallets
    #######################
    def scene3_non_deterministic_wallets(self):
        # Scene 3: Explaining Non-Deterministic Wallets
        self.explain_non_deterministic_wallets()
    
    def explain_non_deterministic_wallets(self):
        # Use the elements from the previous scene for continuity
        title = self.non_deterministic_title

        
        # 1️⃣ A Bitcoin wallet icon appears at the center of the screen
        wallet_rect = RoundedRectangle(
            height=3.5, width=5,
            corner_radius=0.2,
            fill_opacity=0.3,  # More transparent
            fill_color=BLACK,
            stroke_color=RED,
            stroke_width=3
        )
        wallet_rect.move_to(ORIGIN)
        
        # Bitcoin logo on wallet - using SVG instead of simple circle
        bitcoin_logo = SVGMobject("assets/bitcoin-logo.svg")
        bitcoin_logo.scale(0.3)
        bitcoin_logo.set_color("#f7931a")  # Set to Bitcoin orange color
        bitcoin_logo.move_to(wallet_rect.get_center() + UP * 1.3)  # Inside the wallet
        
        wallet = VGroup(wallet_rect, bitcoin_logo)
        
        # Animate the wallet growing from the center
        self.play(FadeIn(wallet, scale=1.1), run_time=1)
        self.wait(0.5)
        
        # 2️⃣ Keys appear inside the wallet in a grid layout
        keys = VGroup()
        key_labels = VGroup()
        num_keys = 5
        
        # Calculate grid positions for evenly spaced keys
        rows = 2
        cols = 3
        
        # Calculate spacing within wallet boundaries
        h_spacing = wallet_rect.width * 0.6 / (cols - 1) if cols > 1 else 0
        v_spacing = wallet_rect.height * 0.5 / (rows - 1) if rows > 1 else 0
        
        # Starting position (top-left of grid)
        start_x = wallet_rect.get_center()[0] - h_spacing * (cols - 1) / 2
        start_y = wallet_rect.get_center()[1] + v_spacing * (rows - 1) / 2 - 0.3  # Offset to center in wallet
        
        # Create and animate each key appearing in grid
        key_count = 0
        for i in range(rows):
            for j in range(cols):
                if key_count >= num_keys:
                    break
                    
                # Calculate position in grid
                x_pos = start_x + j * h_spacing
                y_pos = start_y - i * v_spacing
                
                key = self.create_key_icon(color=RED_C)
                key.move_to([x_pos, y_pos, 0])
                
                # Add key label
                label = Text(f"Key {key_count+1}", font_size=16, color=WHITE)
                label.next_to(key, DOWN, buff=0.15)
                
                # Ensure label stays inside wallet
                if label.get_bottom()[1] < wallet_rect.get_bottom()[1] + 0.2:
                    label.next_to(key, RIGHT, buff=0.15)
                
                # Animate key and label appearing
                self.play(
                    FadeIn(key, scale=1.2),
                    FadeIn(label),
                    run_time=0.4
                )
                
                keys.add(key)
                key_labels.add(label)
                key_count += 1
                
                if key_count >= num_keys:
                    break
        
        self.wait(0.7)
        
        # 3️⃣ Text box explaining independent generation
        explanation = Text(
            "Each key is independently generated from a random number.",
            font_size=24,
            color=WHITE
        )
        explanation.next_to(wallet, DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(1)
        
        # 4️⃣ Emphasis text box
        emphasis = Text(
            "The keys are NOT RELATED to each other!",
            font_size=28,
            color=RED,
            weight=BOLD
        )
        emphasis.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(emphasis), run_time=1.5)
        
        # Wallet shakes slightly to highlight the issue
        self.play(
            wallet.animate.shift(RIGHT * 0.1),
            run_time=0.1
        )
        self.play(
            wallet.animate.shift(LEFT * 0.2),
            run_time=0.1
        )
        self.play(
            wallet.animate.shift(RIGHT * 0.1),
            run_time=0.1
        )
        
        self.wait(1)
        
        # Group all elements for reference
        main_elements = VGroup(
            title, wallet, keys, key_labels, explanation, emphasis
        )
        
        # Move everything to the left to make room for the warning panel
        self.play(
            main_elements.animate.scale(0.9).shift(LEFT * 2.5),
            run_time=1
        )
        
        # 5️⃣ Red warning panel slides in
        warning_panel = Rectangle(
            height=6, width=4,
            fill_opacity=0.9,
            fill_color=RED_E,
            stroke_color=RED,
            stroke_width=2
        )
        warning_panel.to_edge(RIGHT, buff=0)
        
        # 6️⃣ Warning panel content with improved styling
        # Title bar with black background
        title_bar = Rectangle(
            width=warning_panel.width,
            height=0.8,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        title_bar.move_to(warning_panel.get_top() - DOWN * 0.4)
        
        # Larger, more prominent title
        warning_title = Text("THIS IS BAD", font_size=42, color=BLACK, weight=BOLD)
        warning_title.move_to(title_bar.get_center())
        
        # Warning icons - using SVG instead of text symbols
        # You'll need to create these SVG files in your assets folder
        warning1_icon = SVGMobject("assets/warning-icon.svg")
        warning1_icon.set_color(WHITE)
        warning1_icon.scale(0.4)
        
        warning1_text = Text(
            "You must keep copies of all keys",
            font_size=24,  # Increased font size
            color=WHITE
        )
        warning1_text.next_to(warning1_icon, RIGHT, buff=0.2)
        warning1 = VGroup(warning1_icon, warning1_text)
        warning1.arrange(RIGHT, aligned_edge=UP)
        warning1.next_to(title_bar, DOWN, buff=0.6)  # Position below title bar
        warning1.shift(RIGHT * 0.2)  # Slight right shift for better alignment
        
        # Second line for first warning
        warning1_text2 = Text(
            "you generated.",
            font_size=24,  # Increased font size
            color=WHITE
        )
        warning1_text2.next_to(warning1, DOWN, buff=0.1)
        warning1_text2.align_to(warning1_text, LEFT)
        
        warning2_icon = SVGMobject("assets/warning-icon.svg")
        warning2_icon.set_color(WHITE)
        warning2_icon.scale(0.4)
        
        warning2_text = Text(
            "Frequent backups are required.",
            font_size=24,  # Increased font size
            color=WHITE
        )
        warning2_text.next_to(warning2_icon, RIGHT, buff=0.2)
        warning2 = VGroup(warning2_icon, warning2_text)
        warning2.arrange(RIGHT, aligned_edge=UP)
        
        # Position the second warning below the first warning's second line
        warning2.next_to(warning1_text2, DOWN, buff=0.5)
        warning2.align_to(warning1, LEFT)
        
        # Group all warning content
        warning_content = VGroup(warning_title, warning1, warning1_text2, warning2)
        
        # Ensure content fits within panel
        max_width = warning_panel.width - 0.4  # Leave some margin
        if warning_content.width > max_width:
            scale_factor = max_width / warning_content.width
            warning_content.scale(scale_factor)
        
        warning_content.move_to(warning_panel.get_center())
        
        # Animate panel sliding in
        warning_group = VGroup(warning_panel, warning_title)
        warning_group.shift(RIGHT * warning_panel.width)  # Start off-screen
        
        self.play(
            warning_group.animate.shift(LEFT * warning_panel.width),
            run_time=1
        )
        
        # Animate each warning element appearing one by one
        self.wait(0.5)
        self.play(FadeIn(warning1), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(warning1_text2), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(warning2), run_time=0.8)
        
        self.wait(1)
        
        # 7️⃣ Warning panel pulses
        self.play(
            warning_panel.animate.scale(1.05),
            run_time=0.5
        )
        self.play(
            warning_panel.animate.scale(1/1.05),
            run_time=0.5
        )
        
        self.wait(1)
        
        # 8️⃣ Warning panel slides out
        warning_full_group = VGroup(warning_panel, warning_title, warning1, warning1_text2, warning2)
        self.play(
            warning_full_group.animate.shift(RIGHT * warning_panel.width),
            run_time=1
        )
        
        # Move main elements back to center
        self.play(
            main_elements.animate.scale(1/0.9).shift(RIGHT * 2.5),
            run_time=1
        )
        
        # 9️⃣ Screen fades to black
        self.play(FadeOut(main_elements), run_time=1)
        
        # 🔟 Text for next scene fades in
        next_scene_text = Text(
            "Deterministic Wallets (The Better Way)",
            font_size=48,
            color=BLUE
        )
        next_scene_text.move_to(ORIGIN)
        
        self.play(FadeIn(next_scene_text), run_time=1.5)
        self.wait(1)
        
        # Fade out for transition to next scene
        self.play(FadeOut(next_scene_text), run_time=1)

    def create_key_icon(self, color=BLUE):
        # Load SVG file from assets folder
        key = SVGMobject("assets/key.svg")
        
        # Set color
        key.set_color(color)
        
        # Scale appropriately - increased size for better visibility
        key.scale(0.3)
        
        return key

    def create_deterministic_wallet_icon(self):
        # Create a representation of deterministic wallet (seed generating multiple keys)
        seed = Circle(radius=0.4, fill_opacity=1, fill_color=BLUE, stroke_width=2, stroke_color=WHITE)
        seed_label = Text("SEED", font_size=20, color=WHITE)
        seed_label.move_to(seed.get_center())
        
        # Create keys with better spacing and arrangement
        keys = VGroup()
        num_keys = 4
        
        # Calculate angles for a more structured, tree-like formation
        angles = []
        start_angle = -PI/3
        end_angle = PI/3
        for i in range(num_keys):
            angle = start_angle + i * (end_angle - start_angle)/(num_keys-1)
            angles.append(angle)
        
        # Create keys at calculated positions
        for angle in angles:
            key = self.create_key_icon(color=BLUE_C)
            # Position keys further from seed for better visibility
            distance = 1.8
            key.move_to(seed.get_center() + distance * np.array([np.cos(angle), np.sin(angle), 0]))
            keys.add(key)
        
        # Create arrows from seed to keys with better visibility
        arrows = VGroup()
        for key in keys:
            arrow = Arrow(
                start=seed.get_center(),
                end=key.get_center(),
                buff=0.2,
                color=BLUE_B,
                stroke_width=2.5
            )
            arrows.add(arrow)
        
        deterministic_icon = VGroup(seed, seed_label, arrows, keys)
        return deterministic_icon

    def create_non_deterministic_wallet_icon(self):
        # Create a representation of non-deterministic wallet (separate keys)
        wallet_rect = RoundedRectangle(
            height=2, width=3,
            corner_radius=0.2,
            fill_opacity=0.5,
            fill_color=RED_D,
            stroke_color=RED,
            stroke_width=2
        )
        
        # Create separate keys with better spacing
        keys = VGroup()
        num_keys = 4  # Changed from 3 to 4 keys
        
        # Calculate positions for evenly spaced keys
        key_spacing = 0.6  # Increased spacing to accommodate 4 keys
        total_width = (num_keys - 1) * key_spacing
        
        for i in range(num_keys):
            key = self.create_key_icon(color=RED_C)
            x_pos = (i - (num_keys-1)/2) * key_spacing
            # Position keys slightly higher in the wallet rectangle for better visibility
            key.move_to(wallet_rect.get_center() + np.array([x_pos, 0.1, 0]))
            keys.add(key)
        
        non_deterministic_icon = VGroup(wallet_rect, keys)
        return non_deterministic_icon

if __name__ == "__main__":
    # This allows the script to be run directly
    # To render the animation: python hd-wallet.py
    
    import sys
    from manim.cli.render.commands import render
    
    # Set up rendering with medium quality and preview
    sys.argv = ["manim", "hd-wallet.py", "BitcoinWalletAnimation", "-pql"]
    render()
