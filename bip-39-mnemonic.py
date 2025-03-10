from manim import *
import random
import hashlib

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
        self.scene4_deterministic_wallets()
        self.scene5_mnemonic_generation()

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
        
        # Animate the question appearance - FASTER
        self.play(Write(question_line1), run_time=1.0)  # Reduced from 1.5
        self.play(Write(question_line2), run_time=1.0)  # Reduced from 1.5
        
        # Wait for the viewer to read - SHORTER
        self.wait(2)  # Reduced from 3
        
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
        self.wait(0.5)  # Reduced from 1
        
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
            run_time=1.0  # Reduced from 1.5
        )
        self.play(
            Write(deterministic),
            Write(non_deterministic),
            run_time=1.0  # Reduced from 1.5
        )
        
        self.wait(0.5)  # Reduced from 1
        
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
            run_time=1.0  # Reduced from 1.5
        )
        
        self.wait(0.5)  # Reduced from 1
        
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
            run_time=1.0  # Reduced from 1.5
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
        self.play(FadeIn(wallet, scale=1.1), run_time=0.7)  # Reduced from 1
        self.wait(0.3)  # Reduced from 0.5
        
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
                    run_time=0.3  # Reduced from 0.4
                )
                
                keys.add(key)
                key_labels.add(label)
                key_count += 1
                
                if key_count >= num_keys:
                    break
        
        self.wait(0.5)  # Reduced from 0.7
        
        # 3️⃣ Text box explaining independent generation
        explanation = Text(
            "Each key is independently generated from a random number.",
            font_size=24,
            color=WHITE
        )
        explanation.next_to(wallet, DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=1.0)  # Reduced from 1.5
        self.wait(0.7)  # Reduced from 1
        
        # 4️⃣ Emphasis text box
        emphasis = Text(
            "The keys are NOT RELATED to each other!",
            font_size=28,
            color=RED,
            weight=BOLD
        )
        emphasis.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(emphasis), run_time=1.0)  # Reduced from 1.5
        
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
        
        self.wait(0.7)  # Reduced from 1
        
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
            run_time=0.7  # Reduced from 1
        )
        
        # Animate each warning element appearing one by one
        self.wait(0.3)  # Reduced from 0.5
        self.play(FadeIn(warning1), run_time=0.6)  # Reduced from 0.8
        self.wait(0.2)  # Reduced from 0.3
        self.play(FadeIn(warning1_text2), run_time=0.6)  # Reduced from 0.8
        self.wait(0.2)  # Reduced from 0.3
        self.play(FadeIn(warning2), run_time=0.6)  # Reduced from 0.8
        
        self.wait(0.7)  # Reduced from 1
        
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
        
        # 8️⃣ Warning panel slides out while main elements fade out simultaneously
        warning_full_group = VGroup(warning_panel, warning_title, warning1, warning1_text2, warning2)
        
        # Animate both actions at the same time
        self.play(
            warning_full_group.animate.shift(RIGHT * warning_panel.width),
            FadeOut(main_elements),
            run_time=1.0
        )
        
        # 🔟 Text for next scene fades in
        next_scene_text = Text(
            "Deterministic Wallets (The Better Way)",
            font_size=48,
            color=BLUE
        )
        next_scene_text.move_to(ORIGIN)
        
        self.play(FadeIn(next_scene_text), run_time=1.0)  # Reduced from 1.5
        self.wait(0.7)  # Reduced from 1
        
        # Fade out for transition to next scene
        self.play(FadeOut(next_scene_text), run_time=1)

    #######################
    # SCENE 4: Deterministic Wallets
    #######################
    def scene4_deterministic_wallets(self):
        # Scene 4: Explaining Deterministic Wallets as the better approach
        self.explain_deterministic_wallets()
    
    def explain_deterministic_wallets(self):
        # Use the transition text from the previous scene
        title = Text("Deterministic Wallets (The Better Way)", font_size=48, color=BLUE)
        title.to_edge(UP, buff=1)
        
        # We already faded in this title at the end of scene 3, so we'll start with it
        # and animate it moving to the top position
        self.play(
            title.animate.to_edge(UP, buff=1),
            run_time=0.7  # Reduced from 1
        )
        self.wait(0.3)  # Reduced from 0.5
        
        # 1️⃣ A Bitcoin wallet icon appears in the center
        wallet_rect = RoundedRectangle(
            height=4, width=5,  # Increased height to fit all keys inside
            corner_radius=0.2,
            fill_opacity=0.3,
            fill_color=BLUE_D,
            stroke_color=BLUE,
            stroke_width=3
        )
        wallet_rect.move_to(ORIGIN)
        
        # Bitcoin logo on wallet - using SVG instead of simple circle
        bitcoin_logo = SVGMobject("assets/bitcoin-logo.svg")
        bitcoin_logo.scale(0.25)
        bitcoin_logo.set_color("#f7931a")  # Set to Bitcoin orange color
        bitcoin_logo.move_to(wallet_rect.get_center() + UP * 1)
        
        wallet = VGroup(wallet_rect, bitcoin_logo)
        
        # Animate the wallet growing from the center
        self.play(FadeIn(wallet, scale=1.1), run_time=0.7)  # Reduced from 1
        self.wait(0.3)  # Reduced from 0.5
        
        # 2️⃣ Inside the wallet, a single black box labeled "Seed" appears
        seed_box = Rectangle(
            height=0.8, width=1.5,
            fill_opacity=1,
            fill_color=BLACK,
            stroke_color=YELLOW,
            stroke_width=2
        )
        # Position seed at the top area of the wallet
        seed_box.move_to(wallet_rect.get_center() + UP * 1.2)
        
        seed_label = Text("SEED", font_size=28, color=YELLOW)
        seed_label.move_to(seed_box.get_center())
        
        seed = VGroup(seed_box, seed_label)
        
        self.play(FadeIn(seed, scale=1.2))
        self.wait(0.3)  # Reduced from 0.5
        
        # 3️⃣ From the seed, arrows start growing, pointing to multiple new keys
        keys = VGroup()
        key_labels = VGroup()
        arrows = VGroup()
        num_keys = 5
        
        # Calculate positions for keys in a hierarchical tree format below the seed
        # Ensure all keys are inside the wallet boundaries
        
        # Define wallet boundaries
        wallet_top = wallet_rect.get_center()[1] + wallet_rect.height/2
        wallet_bottom = wallet_rect.get_center()[1] - wallet_rect.height/2
        wallet_left = wallet_rect.get_center()[0] - wallet_rect.width/2
        wallet_right = wallet_rect.get_center()[0] + wallet_rect.width/2
        
        # Calculate safe area inside wallet (with margin)
        margin = 0.3
        safe_top = wallet_top - margin
        safe_bottom = wallet_bottom + margin
        safe_left = wallet_left + margin
        safe_right = wallet_right - margin
        
        # Position keys in a fan/tree layout below the seed
        key_positions = []
        
        # Calculate vertical position for keys (lower than seed)
        key_y = seed_box.get_center()[1] - 1.5  # Position keys below the seed
        
        # Ensure keys are above the bottom of the wallet
        if key_y < safe_bottom:
            key_y = safe_bottom + 0.5
        
        # Calculate horizontal spacing for keys
        total_width = safe_right - safe_left - 0.6  # Leave some margin on sides
        key_spacing = total_width / (num_keys - 1) if num_keys > 1 else 0
        
        # Generate positions for each key
        for i in range(num_keys):
            x_pos = safe_left + 0.3 + i * key_spacing
            key_positions.append(np.array([x_pos, key_y, 0]))
        
        # Create and animate each key appearing with its connecting arrow
        for i in range(num_keys):
            # Create key
            key = self.create_key_icon(color=BLUE_C)
            key.move_to(key_positions[i])
            
            # Add key label
            label = Text(f"Key {i+1}", font_size=16, color=WHITE)
            label.next_to(key, DOWN, buff=0.2)
            
            # Ensure label is inside wallet
            if label.get_bottom()[1] < safe_bottom:
                label.next_to(key, RIGHT, buff=0.15)
            
            # Create arrow from seed to key
            arrow = Arrow(
                start=seed_box.get_bottom() + DOWN * 0.1,
                end=key.get_top() + UP * 0.1,
                buff=0.1,
                color=BLUE_B,
                stroke_width=2
            )
            
            # Animate arrow growing from seed to key position
            self.play(GrowArrow(arrow), run_time=0.3)  # Reduced from 0.5
            
            # Animate key and label appearing
            self.play(
                FadeIn(key, scale=1.2),
                FadeIn(label),
                run_time=0.3  # Reduced from 0.5
            )
            
            keys.add(key)
            key_labels.add(label)
            arrows.add(arrow)
            
            # Brief pause after first key to emphasize the pattern
            if i == 0:
                self.wait(0.2)  # Reduced from 0.3
        
        self.wait(0.7)  # Reduced from 1
        
        # Create a text box with a background for better visual connection
        text_box = Rectangle(
            width=7, height=1.2,
            fill_color=BLACK,
            fill_opacity=0.7,
            stroke_width=1,
            stroke_color=BLUE_D,
            stroke_opacity=0.5
        )
        text_box.move_to(DOWN * 2.5)
        
        # 4️⃣ Text box explaining the concept
        explanation = Text(
            "All keys are derived from a single seed.",
            font_size=28,
            color=YELLOW
        )
        explanation.move_to(text_box.get_center())
        
        # Animate the text box appearing first
        self.play(FadeIn(text_box), run_time=0.5)  # Reduced from 0.7
        
        # Then write the explanation
        self.play(Write(explanation), run_time=1.0)  # Reduced from 1.5
        self.wait(0.7)  # Reduced from 1
        
        # 5️⃣ Green checkmark appears next to the wallet
        checkmark = Text("✓", font_size=72, color=GREEN)
        checkmark.next_to(wallet, RIGHT, buff=0.5)
        
        self.play(FadeIn(checkmark, scale=1.5))
        self.wait(0.7)  # Reduced from 1
        
        # Group text box and explanation
        text_elements = VGroup(text_box, explanation)
        
        # Move everything to the left to make room for benefits panel
        main_elements = VGroup(
            title, wallet, seed, keys, key_labels, arrows, 
            text_elements, checkmark
        )
        
        self.play(
            main_elements.animate.scale(0.9).shift(LEFT * 2.5),
            run_time=1
        )
        
        # Benefits panel slides in from the right
        benefits_panel = Rectangle(
            height=6, width=4,
            fill_opacity=0.9,
            fill_color=GREEN_E,
            stroke_color=GREEN,
            stroke_width=2
        )
        benefits_panel.to_edge(RIGHT, buff=0)
        
        # Title bar with black background
        title_bar = Rectangle(
            width=benefits_panel.width,
            height=0.8,
            fill_color=BLACK,
            fill_opacity=1,
            stroke_width=0
        )
        title_bar.move_to(benefits_panel.get_top() - DOWN * 0.4)
        
        # Benefits title
        benefits_title = Text("ADVANTAGES", font_size=36, color=WHITE, weight=BOLD)
        benefits_title.move_to(title_bar.get_center())
        
        # Benefits with checkmarks
        benefit1_icon = Text("✓", font_size=28, color=WHITE)
        benefit1_text = Text(
            "Only need to backup the seed once",
            font_size=20,
            color=WHITE
        )
        benefit1 = VGroup(benefit1_icon, benefit1_text)
        benefit1.arrange(RIGHT, aligned_edge=UP, buff=0.2)
        benefit1.next_to(title_bar, DOWN, buff=0.6)
        benefit1.shift(RIGHT * 0.2)
        
        benefit2_icon = Text("✓", font_size=28, color=WHITE)
        benefit2_text = Text(
            "Can generate unlimited keys",
            font_size=20,
            color=WHITE
        )
        benefit2 = VGroup(benefit2_icon, benefit2_text)
        benefit2.arrange(RIGHT, aligned_edge=UP, buff=0.2)
        benefit2.next_to(benefit1, DOWN, buff=0.5)
        benefit2.align_to(benefit1, LEFT)
        
        benefit3_icon = Text("✓", font_size=28, color=WHITE)
        benefit3_text = Text(
            "Keys are organized in a",
            font_size=20,
            color=WHITE
        )
        benefit3 = VGroup(benefit3_icon, benefit3_text)
        benefit3.arrange(RIGHT, aligned_edge=UP, buff=0.2)
        benefit3.next_to(benefit2, DOWN, buff=0.5)
        benefit3.align_to(benefit1, LEFT)
        
        # Second line for third benefit
        benefit3_text2 = Text(
            "predictable way",
            font_size=20,
            color=WHITE
        )
        benefit3_text2.next_to(benefit3, DOWN, buff=0.1)
        benefit3_text2.align_to(benefit3_text, LEFT)
        
        # Group all benefits content
        benefits_content = VGroup(title_bar, benefits_title, benefit1, benefit2, benefit3, benefit3_text2)
        
        # Ensure content fits within panel
        max_width = benefits_panel.width - 0.4  # Leave some margin
        if benefits_content.width > max_width:
            scale_factor = max_width / benefits_content.width
            benefits_content.scale(scale_factor)
        
        benefits_content.move_to(benefits_panel.get_center())
        
        # Animate panel sliding in
        benefits_group = VGroup(benefits_panel, title_bar, benefits_title)
        benefits_group.shift(RIGHT * benefits_panel.width)  # Start off-screen
        
        self.play(
            benefits_group.animate.shift(LEFT * benefits_panel.width),
            run_time=1
        )
        
        # Animate each benefit appearing one by one
        self.wait(0.3)  # Reduced from 0.5
        self.play(FadeIn(benefit1), run_time=0.6)  # Reduced from 0.8
        self.wait(0.2)  # Reduced from 0.3
        self.play(FadeIn(benefit2), run_time=0.6)  # Reduced from 0.8
        self.wait(0.2)  # Reduced from 0.3
        self.play(FadeIn(benefit3), run_time=0.6)  # Reduced from 0.8
        self.wait(0.1)  # Reduced from 0.2
        self.play(FadeIn(benefit3_text2), run_time=0.6)  # Reduced from 0.8
        
        self.wait(0.7)  # Reduced from 1
        
        # Benefits panel pulses
        self.play(
            benefits_panel.animate.scale(1.05),
            run_time=0.5
        )
        self.play(
            benefits_panel.animate.scale(1/1.05),
            run_time=0.5
        )
        
        self.wait(1)
        
        # Benefits panel slides out while main elements fade out simultaneously
        benefits_full_group = VGroup(benefits_panel, benefits_content)
        
        # Animate both actions at the same time
        self.play(
            benefits_full_group.animate.shift(RIGHT * benefits_panel.width),
            FadeOut(main_elements),
            run_time=1.0
        )
        
        self.wait(0.3)  # Reduced from 0.5
        
        # 7️⃣ The text "How are mnemonic words created?" fades in
        next_scene_text = Text(
            "How are mnemonic words created?",
            font_size=42,
            color=YELLOW
        )
        next_scene_text.move_to(ORIGIN)  # Changed from to_edge(DOWN) to center
        
        self.play(FadeIn(next_scene_text), run_time=1.0)  # Reduced from 1.5
        self.wait(0.7)  # Reduced from 1
        
        # Fade out for transition to next scene
        self.play(
            FadeOut(next_scene_text),
            run_time=1
        )

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

    def create_key_icon(self, color=BLUE):
        # Load SVG file from assets folder
        key = SVGMobject("assets/key.svg")
        
        # Set color
        key.set_color(color)
        
        # Scale appropriately - increased size for better visibility
        key.scale(0.3)
        
        return key



    #######################
    # SCENE 5: Mnemonic Generation (BIP-39)
    #######################
    def scene5_mnemonic_generation(self):
        # Step 1: Generate Entropy
        self.generate_entropy_animation()
        
        # Step 2: Hash the Entropy
        self.hash_entropy_animation()
        
        # Step 3: Combine Entropy and Checksum
        self.combine_entropy_and_checksum_animation()
        
        # Step 4: Split into 11-bit Segments and Map to Words
        self.split_and_map_to_words_animation()
        
    
    def generate_entropy_animation(self):
        # Step 1 title
        title = Text("Step 1: Generate Entropy (130 bits)", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)  # Faster title write
        self.wait(0.2)  # Reduced wait time
        
        # Create a container for the binary digits - made larger
        container = Rectangle(
            width=13, height=7,
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.2
        )
        container.next_to(title, DOWN, buff=0.6)
        
        # Create initial binary display with all zeros
        binary_rows = []
        for i in range(5):  # 5 rows for 130 bits
            row = Text("0" * 26, font_size=28)  # Increased font size
            if i == 0:
                row.move_to(container.get_center() + UP * 1.4)
            else:
                row.next_to(binary_rows[i-1], DOWN, buff=0.2)
            binary_rows.append(row)
        
        binary_group = VGroup(*binary_rows)
        binary_group.move_to(container.get_center())
        
        # Add "entropy = " label with larger font
        entropy_label = Text("entropy = ", font_size=28, color=BLUE_B)
        entropy_label.next_to(binary_group, LEFT, buff=0.3)
        
        # Make sure it's still inside the container
        if entropy_label.get_left()[0] < container.get_left()[0] + 0.2:
            entropy_label.shift(RIGHT * (container.get_left()[0] + 0.2 - entropy_label.get_left()[0]))
        
        # Animate the container appearance with a glow effect - faster
        glow = container.copy().set_stroke(color=BLUE, width=8, opacity=0.8)
        
        self.play(
            Create(container),
            FadeIn(glow, rate_func=there_and_back),
            run_time=0.7  # Faster animation
        )
        self.play(
            FadeIn(binary_group),
            Write(entropy_label),
            run_time=0.5  # Faster animation
        )
        self.wait(0.2)  # Reduced wait time
        
        # Improved entropy generation animation - faster transitions
        for transition in range(3):  # Reduced to 3 transitions for speed
            # Generate new random binary for all rows
            new_rows = []
            for i in range(5):
                # Create a new row with random bits
                new_text = ''.join(random.choice(["0", "1"]) for _ in range(26))
                new_row = Text(new_text, font_size=28)
                
                if i == 0:
                    new_row.move_to(container.get_center() + UP * 1.4)
                else:
                    new_row.next_to(new_rows[i-1], DOWN, buff=0.2)
                new_rows.append(new_row)
            
            new_group = VGroup(*new_rows)
            new_group.move_to(container.get_center())
            
            # More dynamic transition between states - faster
            if transition == 0:
                self.play(
                    TransformFromCopy(binary_group, new_group),
                    FadeOut(binary_group),
                    run_time=0.5  # Faster animation
                )
            else:
                # Add some visual effects to show randomness - faster
                flash = container.copy().set_fill(BLUE_A, opacity=0.3)
                self.play(
                    FadeIn(flash, rate_func=there_and_back, run_time=0.2),  # Faster flash
                    ReplacementTransform(binary_group, new_group, run_time=0.5)  # Faster transform
                )
            
            # Update binary_group to the new state
            binary_group = new_group
            
            self.wait(0.1)  # Reduced wait time
        
        # Generate the final 130-bit entropy (trimming to exactly 130 bits)
        final_entropy = ""
        for _ in range(130):
            final_entropy += random.choice(["0", "1"])
        
        # Format the final entropy into 5 rows (first 4 rows with 26 bits, last row with 24 bits)
        final_rows = []
        for i in range(4):  # First 4 rows
            row_text = final_entropy[i*26:(i+1)*26]  # 26 bits per row
            row = Text(row_text, font_size=28, color=GREEN_B)
            if i == 0:
                row.move_to(container.get_center() + UP * 1.4)
            else:
                row.next_to(final_rows[i-1], DOWN, buff=0.2)
            final_rows.append(row)
        
        # Last row with remaining 24 bits
        last_row_text = final_entropy[104:130]  # Last 24 bits
        last_row = Text(last_row_text, font_size=28, color=GREEN_B)
        last_row.next_to(final_rows[3], DOWN, buff=0.2)
        final_rows.append(last_row)
        
        final_group = VGroup(*final_rows)
        final_group.move_to(container.get_center())
        
        # Highlight the final entropy with a special effect - faster
        highlight = container.copy().set_stroke(color=GREEN, width=6)
        
        # Replace the random bits with the final entropy - faster
        self.play(
            FadeOut(binary_group),
            FadeIn(final_group),
            FadeIn(highlight, rate_func=there_and_back),
            run_time=0.7  # Faster animation
        )
        
        # Add a label for the final entropy - faster
        final_label = Text("Final Entropy Generated", font_size=36, color=GREEN)
        final_label.next_to(container, DOWN, buff=0.5)
        
        self.play(
            Write(final_label),
            container.animate.set_stroke(color=GREEN_B, width=3),
            run_time=0.5  # Faster animation
        )
        self.wait(0.5)  # Reduced wait time
        
        # Store the final entropy for later use
        self.entropy = final_entropy[:130]  # Ensure exactly 130 bits
        self.entropy_display = VGroup(container, final_group, final_label, entropy_label)
        
        # Fade out Step 1 elements
        self.play(
            FadeOut(title),
            FadeOut(self.entropy_display),
            run_time=0.7
        )

    def hash_entropy_animation(self):
        # Step 2 title
        title = Text("Step 2: Hash the Entropy", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        self.wait(0.2)
        
        # Create a simplified version of the entropy for display
        entropy_sample = self.entropy[:3] + "..." + self.entropy[-3:]
        
        # Create the SHA-256 hash function display
        hash_function = Text("SHA256(", font_size=40, color=WHITE)
        entropy_text = Text(f'"{entropy_sample}"', font_size=36, color=BLUE_B)
        closing_paren = Text(")", font_size=40, color=WHITE)
        
        # Position the hash function elements - moved further left
        hash_function.shift(LEFT * 6)
        entropy_text.next_to(hash_function, RIGHT, buff=0.1)
        closing_paren.next_to(entropy_text, RIGHT, buff=0.1)
        
        # Add equals sign
        equals = Text("=", font_size=40, color=WHITE)
        equals.next_to(closing_paren, RIGHT, buff=0.5)
        
        # Group the left side of the equation and position it more centrally
        left_side = VGroup(hash_function, entropy_text, closing_paren, equals)
        left_side.move_to(ORIGIN).shift(LEFT * 2.5).shift(UP * 0.5)  # Moved left and down
        
        # Create a brace to indicate "Message/file"
        message_brace = Brace(entropy_text, DOWN, color=BLUE_B)
        message_label = Text("Entropy", font_size=32, color=BLUE_B)
        message_label.next_to(message_brace, DOWN, buff=0.2)
        
        # Animate the appearance of the hash function
        self.play(
            Write(hash_function),
            Write(entropy_text),
            Write(closing_paren),
            Write(equals),
            run_time=0.8
        )
        
        self.play(
            GrowFromCenter(message_brace),
            Write(message_label),
            run_time=0.6
        )
        
        self.wait(0.3)
        
        # Calculate the actual SHA-256 hash of the entropy
        entropy_bytes = int(self.entropy, 2).to_bytes((len(self.entropy) + 7) // 8, byteorder='big')
        hash_result = hashlib.sha256(entropy_bytes).hexdigest()
        
        # Convert hash to binary for display
        hash_binary = bin(int(hash_result, 16))[2:].zfill(256)
        
        # Create the hash result display (in binary)
        hash_rows = []
        for i in range(8):  # 8 rows for 256 bits
            row_text = hash_binary[i*32:(i+1)*32]  # 32 bits per row
            row = Text(row_text, font_size=24, color=YELLOW)
            
            if i == 0:
                row.next_to(equals, RIGHT, buff=0.3)  # Reduced buffer to bring closer to equals
            else:
                row.next_to(hash_rows[i-1], DOWN, buff=0.1)
            
            hash_rows.append(row)
        
        hash_group = VGroup(*hash_rows)
        
        # Center the hash result with the equals sign, but closer
        hash_group.move_to(equals.get_center() + RIGHT * 3.5)  # Reduced from 4 to 3.5
        
        # Create a brace for "Hash result"
        output_brace = Brace(hash_group, DOWN, color=YELLOW)
        output_label = Text("Hash result", font_size=32, color=YELLOW)
        output_label.next_to(output_brace, DOWN, buff=0.2)
        
        # Animate the hash calculation with a visual effect
        hash_box = SurroundingRectangle(entropy_text, color=BLUE, buff=0.2)
        self.play(Create(hash_box), run_time=0.5)
        
        # Create a moving particle effect to represent the hashing process
        dot = Dot(color=BLUE_A).move_to(entropy_text.get_center())
        self.play(
            dot.animate.scale(3).set_color(YELLOW),
            run_time=0.7
        )
        
        # Reveal the hash result
        self.play(
            FadeOut(dot),
            FadeOut(hash_box),
            Write(hash_rows[0]),
            run_time=0.5
        )
        
        for i in range(1, 8):
            self.play(Write(hash_rows[i]), run_time=0.2)
        
        self.play(
            GrowFromCenter(output_brace),
            Write(output_label),
            run_time=0.6
        )
        
        self.wait(0.5)
        
        # Highlight the checksum (first 4 bits of the hash)
        checksum_box = SurroundingRectangle(
            hash_rows[0][0:4],  # First 4 bits of the first row
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        
        checksum_label = Text("Checksum (4 bits)", font_size=32, color=RED)
        checksum_label.next_to(checksum_box, UP, buff=0.3)
        
        self.play(
            Create(checksum_box),
            Write(checksum_label),
            run_time=0.7
        )
        
        # Explanation text
        checksum_explanation = Text(
            "The first 4 bits of the hash result\nserve as the checksum",
            font_size=28,
            color=RED_B
        )
        checksum_explanation.next_to(output_label, DOWN, buff=0.5)
        
        self.play(Write(checksum_explanation), run_time=0.8)
        self.wait(0.5)
        
        # Store the hash result for later use
        self.hash_result = hash_binary
        self.checksum = hash_binary[:4]  # Store the checksum separately
        self.hash_display = VGroup(
            left_side, hash_group, 
            message_brace, message_label,
            output_brace, output_label,
            checksum_box, checksum_label,
            checksum_explanation
        )
        # Store the title separately for later reference
        self.step2_title = title

    def combine_entropy_and_checksum_animation(self):
        # Fade out step 2 elements except the checksum part
        elements_to_fade = [x for x in self.hash_display if x not in [self.hash_display[7], self.hash_display[6]]]
        
        # Create Step 3 title
        title = Text("Step 3: Combine Entropy with Checksum", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        # Replace the Step 2 title with Step 3 title
        self.play(
            FadeOut(VGroup(*elements_to_fade)),
            ReplacementTransform(self.step2_title, title),
            run_time=0.8
        )
        
        # Create a more dynamic checksum movement
        checksum_value = Text(self.checksum, font_size=36, color=RED)
        checksum_label = Text("Checksum (4 bits)", font_size=32, color=RED)
        
        checksum_group = VGroup(checksum_value, checksum_label)
        checksum_group.arrange(DOWN, buff=0.2)
        checksum_group.next_to(title, DOWN, buff=0.8)
        checksum_group.to_edge(RIGHT, buff=1.5)
        
        # Add a glowing effect during transformation
        glow = checksum_value.copy().set_color(RED_A).set_opacity(0.6).scale(1.2)
        
        self.play(
            FadeTransform(self.hash_display[6], checksum_value),
            FadeTransform(self.hash_display[7], checksum_label),
            FadeIn(glow, rate_func=there_and_back),
            run_time=0.8
        )
        
        # Format entropy rows with improved visual style
        entropy_rows = []
        for i in range(5):
            if i < 4:
                row_text = self.entropy[i*26:(i+1)*26]
            else:
                row_text = self.entropy[104:130]
                
            row = Text(row_text, font_size=22, color=GREEN_B)
            
            if i == 0:
                row.move_to(ORIGIN).shift(UP * 2).shift(LEFT * 2.5)
            else:
                row.next_to(entropy_rows[i-1], DOWN, buff=0.15)
                
            entropy_rows.append(row)
        
        entropy_group = VGroup(*entropy_rows)
        
        entropy_label = Text("Entropy", font_size=32, color=GREEN_B)
        entropy_label.next_to(entropy_group, DOWN, buff=0.3)

        # Animate entropy appearance with cascading effect
        for row in entropy_rows:
            self.play(
                FadeIn(row, shift=RIGHT * 0.3),
                run_time=0.2
            )
        
        self.play(
            Write(entropy_label),
            run_time=0.4
        )

        # Animated plus sign
        plus_sign = Text("+", font_size=48, color=YELLOW)
        plus_sign.move_to((entropy_group.get_right() + checksum_group.get_left())/2)
        
        self.play(
            Write(plus_sign),
            plus_sign.animate.scale(1.2),
            run_time=0.4
        )
        self.play(plus_sign.animate.scale(1/1.2), run_time=0.2)
        
        # Create checksum bits with pulsing effect
        checksum_bits = Text(self.checksum, font_size=22, color=RED)
        checksum_bits.next_to(entropy_rows[-1], RIGHT, buff=0.1)

        # Create combined group first
        combined_group = VGroup(*entropy_rows, checksum_bits)

        # Combined label with dynamic appearance
        combined_label = Text("Entropy + Checksum", font_size=32, color=BLUE)
        combined_label.next_to(entropy_group, DOWN, buff=0.3)
        
        # Animate combination with visual effects
        self.play(
            FadeOut(plus_sign, shift=UP),
            FadeOut(entropy_label),
            ReplacementTransform(checksum_value.copy(), checksum_bits),
            run_time=0.8
        )
        
        # Add highlighting effect to show combination
        highlight = combined_group.copy()
        highlight.set_color(BLUE_A).set_opacity(0.3)
        
        self.play(
            FadeIn(highlight, rate_func=there_and_back),
            Write(combined_label),
            run_time=0.8
        )

        # Add improved explanation with animated appearance
        explanation = VGroup(
            Text("The combined bits will be used", font_size=28, color=YELLOW),
            Text("to derive the mnemonic phrase", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.1)
        explanation.next_to(combined_label, DOWN, buff=0.3)
        
        self.play(
            Write(explanation[0]),
            run_time=0.6
        )
        self.play(
            Write(explanation[1]),
            run_time=0.6
        )
        
        # Final emphasis on the combined result
        final_highlight = combined_group.copy()
        final_highlight.set_color(BLUE).set_opacity(0.3)
        self.play(
            FadeIn(final_highlight, rate_func=there_and_back),
            run_time=1
        )
        
        self.wait(0.5)
        
        # Store the combined bits for later use
        self.combined_bits = self.entropy + self.checksum
        self.combined_display = VGroup(
            combined_group,
            combined_label,
            explanation,
            checksum_group
        )
        
        # Store the title for step 3
        self.step3_title = title

    def split_and_map_to_words_animation(self):
        # Create a smooth transition from Step 3 to Step 4
        # Keep the combined bits on screen while fading out other elements
        self.play(
            FadeOut(self.combined_display[1:]),  # Keep the bits, fade out labels
            FadeOut(self.step3_title),  # Remove Step 3 title
            run_time=0.7
        )
        
        # PART 1: Split into segments animation
        # Create Step 4 title
        title = Text("Step 4: Split into 11-bit Segments", font_size=36, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        self.play(FadeIn(title), run_time=0.7)
        self.wait(0.3)
        
        # Get the combined bits from Step 3
        combined_bits_content = self.combined_display[0]
        
        # Create new formatted display for combined bits with monospace font
        combined_bits_rows = []
        
        # Use monospace font to ensure every bit has the same width
        # Reformat into 4 rows with 33 bits each for better visualization
        for i in range(4):  # Exactly 4 rows
            # Calculate start and end positions for this row
            # Ensure we don't exceed the length of combined_bits
            start_pos = i * 33
            end_pos = min(start_pos + 33, len(self.combined_bits))
            row_text = self.combined_bits[start_pos:end_pos]
            
            # Use monospaced font for equal character spacing
            row = Text(row_text, font_size=16, color=BLUE_B, font="Courier New")
            
            if i == 0:
                row.move_to(UP * 1.8)
            else:
                row.next_to(combined_bits_rows[i-1], DOWN, buff=0.1)
                
            combined_bits_rows.append(row)
        
        combined_bits_display = VGroup(*combined_bits_rows)
        
        # Center the rows horizontally
        for row in combined_bits_rows:
            row.move_to([0, row.get_center()[1], 0])
        
        # Add a label for clarity
        combined_label = Text("Combined bits (Entropy + Checksum):", font_size=18, color=BLUE)
        combined_label.next_to(combined_bits_display, UP, buff=0.1)
        
        # Transform from Step 3 combined bits to the new formatted display
        self.play(
            ReplacementTransform(combined_bits_content, combined_bits_display),
            FadeIn(combined_label), 
            run_time=0.8
        )
        
        # Add row containers to visually show equal bit count
        row_backgrounds = VGroup()
        for row in combined_bits_rows:
            background = SurroundingRectangle(
                row, 
                color=BLUE_E,
                stroke_width=1,
                stroke_opacity=0.3,
                fill_opacity=0.05,
                buff=0.05
            )
            row_backgrounds.add(background)
            
        self.play(FadeIn(row_backgrounds), run_time=0.3)
        
        # Split the combined bits into 11-bit segments
        segments = []
        for i in range(0, len(self.combined_bits), 11):
            if i + 11 <= len(self.combined_bits):
                segments.append(self.combined_bits[i:i+11])
        
        # Position for segment boxes - centered on the screen but shifted left
        start_pos = DOWN * 0.5 + LEFT * 1.5  # Added LEFT component to shift left
        
        # Now extract the segments with animation
        segment_label = Text("11-bit Segments", font_size=22, color=BLUE_C)
        segment_label.next_to(start_pos, UP, buff=0.4)
        
        self.play(Write(segment_label), run_time=0.5)
        
        # Create empty segment boxes first
        segment_boxes = VGroup()
        segment_texts = VGroup()
        
        # Create the grid of empty boxes
        for i in range(len(segments)):
            # Create box for the segment
            box = Rectangle(
                height=0.5, width=1.8,  # Slightly reduced size to "zoom out"
                fill_opacity=0.3,
                fill_color=BLUE_D,
                stroke_color=BLUE,
                stroke_width=2
            )
            
            # Position boxes in a grid layout (4 columns, 3 rows)
            row = i // 4
            col = i % 4
            box.move_to(
                start_pos + 
                RIGHT * (col - 1.5) * 2.0 +  # Reduced spacing between columns (from 2.2 to 2.0)
                DOWN * row * 0.7  # Reduced spacing between rows (from 0.8 to 0.7)
            )
            
            segment_boxes.add(box)
        
        # Animate all empty boxes appearing at once
        self.play(FadeIn(segment_boxes), run_time=0.7)
        
        # Group all the combined bits elements for later reference
        combined_bits_group = VGroup(combined_label, combined_bits_display, row_backgrounds)
        
        # FIRST 3 SEGMENTS: Show detailed extraction animation
        for i in range(3):  # Only do detailed animation for first 3 segments
            segment = segments[i]
            
            # Calculate where this segment is in the original bit string
            start_bit = i * 11
            end_bit = start_bit + 11
            
            # Find which rows and positions contain these bits
            start_row = start_bit // 33
            start_pos_in_row = start_bit % 33
            end_row = end_bit // 33
            end_pos_in_row = end_bit % 33
            
            # Create a list of the characters to highlight
            highlight_chars = []
            
            # If the segment spans multiple rows
            if start_row == end_row:
                # All bits are in one row
                for j in range(start_pos_in_row, end_pos_in_row):
                    highlight_chars.append(combined_bits_rows[start_row][j])
            else:
                # First row - from start position to end of row
                for j in range(start_pos_in_row, 33):
                    highlight_chars.append(combined_bits_rows[start_row][j])
                
                # Second row - from start of row to end position
                for j in range(0, end_pos_in_row):
                    highlight_chars.append(combined_bits_rows[end_row][j])
            
            # Create a VGroup of the characters to highlight
            highlight_group = VGroup(*highlight_chars)
            
            # Highlight the bits in original sequence with yellow color
            self.play(
                highlight_group.animate.set_color(YELLOW),
                run_time=0.4
            )
            
            # Create a temporary visual copy of the segment for animation
            segment_visual = Text(segment, font_size=16, color=YELLOW, font="Courier New")
            segment_visual.move_to(highlight_group.get_center())
            
            # Animate extraction of the segment
            self.play(
                FadeIn(segment_visual),
                run_time=0.3
            )
            
            # Move the segment to its target box
            target_text = Text(segment, font_size=14, color=WHITE, font="Courier New")
            target_text.move_to(segment_boxes[i].get_center())
            
            self.play(
                ReplacementTransform(segment_visual, target_text),
                segment_boxes[i].animate.set_fill(opacity=0.5),
                run_time=0.5
            )
            
            segment_texts.add(target_text)
            
            # Reset the original bits color
            self.play(
                highlight_group.animate.set_color(BLUE_B),
                run_time=0.2
            )
        
        # REMAINING SEGMENTS: Extract with smoother animations but more efficiently
        remaining_segment_visuals = []
        all_remaining_highlights = []
        segment_highlights_map = {}  # To track which bits belong to which segment
        
        # For each remaining segment, collect the bits to highlight
        for i in range(3, len(segments)):
            segment = segments[i]
            start_bit = i * 11
            end_bit = start_bit + 11
            
            # Find which rows and positions contain these bits
            start_row = start_bit // 33
            start_pos_in_row = start_bit % 33
            end_row = end_bit // 33
            end_pos_in_row = end_bit % 33
            
            # Create a list of the characters to highlight
            highlight_chars = []
            
            # If the segment spans multiple rows
            if start_row == end_row:
                # All bits are in one row
                for j in range(start_pos_in_row, end_pos_in_row):
                    highlight_chars.append(combined_bits_rows[start_row][j])
            else:
                # First row - from start position to end of row
                for j in range(start_pos_in_row, 33):
                    highlight_chars.append(combined_bits_rows[start_row][j])
                
                # Second row - from start of row to end position
                for j in range(0, end_pos_in_row):
                    highlight_chars.append(combined_bits_rows[end_row][j])
            
            # Create a VGroup of the characters to highlight for this segment
            segment_highlight = VGroup(*highlight_chars)
            segment_highlights_map[i] = segment_highlight
            
            # Add to our collection of highlights
            all_remaining_highlights.extend(highlight_chars)
        
        # Highlight all remaining bits at once
        remaining_highlights = VGroup(*all_remaining_highlights)
        self.play(
            remaining_highlights.animate.set_color(YELLOW),
            run_time=0.5
        )
        
        # Create temporary visuals for each segment
        for i in range(3, len(segments)):
            segment = segments[i]
            highlight_group = segment_highlights_map[i]
            
            # Create a visual that appears over the highlighted bits
            segment_visual = Text(segment, font_size=16, color=YELLOW, font="Courier New")
            center_pos = highlight_group.get_center()
            segment_visual.move_to(center_pos)
            
            remaining_segment_visuals.append((i, segment_visual))
        
        # Fade in all segment visuals at once
        self.play(
            *[FadeIn(visual) for _, visual in remaining_segment_visuals],
            run_time=0.4
        )
        
        # Now animate all segments moving to their target boxes with a staggered effect
        animations = []
        for i, segment_visual in remaining_segment_visuals:
            segment = segments[i]
            target_text = Text(segment, font_size=14, color=WHITE, font="Courier New")
            target_text.move_to(segment_boxes[i].get_center())
            
            # Add animations for this segment
            animations.append(ReplacementTransform(segment_visual, target_text))
            animations.append(segment_boxes[i].animate.set_fill(opacity=0.5))
            
            # Add the target text to our collection
            segment_texts.add(target_text)
        
        # Play all movement animations at once
        self.play(
            *animations,
            run_time=0.8
        )
        
        # Reset the highlighted bits
        self.play(
            remaining_highlights.animate.set_color(BLUE_B),
            run_time=0.3
        )
        
        # Final pulse effect on all segments to show completion
        self.play(
            *[box.animate.set_stroke(color=YELLOW, width=3) for box in segment_boxes],
            run_time=0.3
        )
        self.play(
            *[box.animate.set_stroke(color=BLUE, width=2) for box in segment_boxes],
            run_time=0.3
        )
        
        # Group all segment elements
        segment_group = VGroup(segment_label, segment_boxes, segment_texts)
        
        # Remove the combined bits to make space
        self.play(
            FadeOut(combined_bits_group),
            run_time=0.5
        )
        
        # Move segments to a higher position
        self.play(
            segment_group.animate.shift(UP * 1.0),
            run_time=0.7
        )
        
        # Change to Step 5 title
        step5_title = Text("Step 5: Map Segments to BIP-39 Words", font_size=36, color=YELLOW)
        step5_title.to_edge(UP, buff=0.5)
        
        self.play(
            FadeOut(title),
            FadeIn(step5_title),
            run_time=0.7
        )
        
        # Create a lookup table visualization - position further right but not at the edge
        lookup_title = Text("BIP-39 Word List", font_size=22, color=YELLOW)
        lookup_title.to_edge(RIGHT, buff=1.0)  # Increased buffer from 0.5 to 1.0
        
        # Position the lookup title to align with the "12 Mnemonic Words" label
        lookup_title.shift(UP * segment_label.get_center()[1] - lookup_title.get_center()[1])
        
        # Create a simplified lookup table
        lookup_table = Rectangle(
            height=2.2, width=3.0,
            fill_opacity=0.5,
            fill_color=DARK_GRAY,
            stroke_color=WHITE,
            stroke_width=2
        )
        lookup_table.next_to(lookup_title, DOWN, buff=0.2)  # Position table below the title
        
        # Sample entries for the lookup table
        table_entries = VGroup(
            Text("00000000000 → abandon", font_size=12, color=WHITE, font="Courier New"),
            Text("00000000001 → ability", font_size=12, color=WHITE, font="Courier New"),
            Text("00000000010 → able", font_size=12, color=WHITE, font="Courier New"),
            Text("...", font_size=12, color=WHITE, font="Courier New"),
            Text("11111111111 → zoo", font_size=12, color=WHITE, font="Courier New")
        )
        table_entries.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        table_entries.move_to(lookup_table.get_center())
        
        # Group all elements
        lookup_group = VGroup(lookup_title, lookup_table, table_entries)
        
        # Animate lookup table appearing
        self.play(
            FadeIn(lookup_group),
            run_time=0.8
        )
        
        # Create and pre-compute all the mnemonic words
        words = []
        for segment in segments:
            # Convert binary segment to integer
            index = int(segment, 2)
            # Use modulo to ensure the index is within range of our sample words
            word = BIP39_WORDS[index % len(BIP39_WORDS)]
            words.append(word)
        
        # Update the segment label
        new_label = Text("12 Mnemonic Words", font_size=22, color=GREEN)
        new_label.move_to(segment_label.get_center())
        
        # FIRST 3 SEGMENTS: Show detailed mapping
        for i in range(3):
            # Highlight the current segment
            self.play(
                segment_boxes[i].animate.set_fill(YELLOW, opacity=0.8),
                segment_texts[i].animate.set_color(BLACK),
                run_time=0.3
            )
            
            # Show arrow from segment to lookup table
            to_lookup_arrow = Arrow(
                start=segment_boxes[i].get_right(),
                end=lookup_table.get_left(),
                buff=0.1,
                color=YELLOW,
                stroke_width=2
            )
            
            self.play(GrowArrow(to_lookup_arrow), run_time=0.2)
            
            # Flash lookup table to indicate searching
            lookup_flash = lookup_table.copy().set_fill(YELLOW, opacity=0.3)
            self.play(
                FadeIn(lookup_flash, rate_func=there_and_back),
                run_time=0.2
            )
            
            # Create word text
            word_text = Text(words[i], font_size=14, color=WHITE)
            word_text.move_to(segment_boxes[i].get_center())
            
            # Replace segment text with word
            self.play(
                FadeOut(segment_texts[i]),
                FadeIn(word_text),
                segment_boxes[i].animate.set_fill(GREEN_D, opacity=0.5).set_stroke(GREEN, width=2),
                run_time=0.3
            )
            
            # Clean up arrow
            self.play(
                FadeOut(to_lookup_arrow),
                run_time=0.2
            )
            
            # Replace the segment text in our collection
            segment_texts[i] = word_text
        
        # After first 3, show that the segments are being transformed to words
        if i == 2:  # After finishing the first 3
            self.play(
                ReplacementTransform(segment_label, new_label),
                run_time=0.5
            )
            segment_label = new_label
        
        # REMAINING SEGMENTS: Map all at once
        # Highlight all remaining segments
        self.play(
            *[segment_boxes[i].animate.set_fill(YELLOW, opacity=0.6) for i in range(3, len(segments))],
            *[segment_texts[i].animate.set_color(BLACK) for i in range(3, len(segments))],
            run_time=0.4
        )
        
        # Flash the lookup table
        self.play(
            FadeIn(lookup_flash, rate_func=there_and_back),
            run_time=0.3
        )
        
        # Create all remaining word texts
        remaining_word_texts = []
        for i in range(3, len(segments)):
            word_text = Text(words[i], font_size=14, color=WHITE)
            word_text.move_to(segment_boxes[i].get_center())
            remaining_word_texts.append((i, word_text))
        
        # Replace all remaining segments with words
        self.play(
            *[FadeOut(segment_texts[i]) for i in range(3, len(segments))],
            *[FadeIn(word_text) for i, word_text in remaining_word_texts],
            *[segment_boxes[i].animate.set_fill(GREEN_D, opacity=0.5).set_stroke(GREEN, width=2) for i in range(3, len(segments))],
            run_time=0.6
        )
        
        # Update segment_texts with the word texts
        for i, word_text in remaining_word_texts:
            segment_texts[i] = word_text
        
        # Final pulse effect on all word boxes
        self.play(
            *[box.animate.set_stroke(color=YELLOW, width=3) for box in segment_boxes],
            run_time=0.3
        )
        self.play(
            *[box.animate.set_stroke(color=GREEN, width=2) for box in segment_boxes],
            run_time=0.3
        )
        
        self.wait(1)



if __name__ == "__main__":
    # This allows the script to be run directly
    # To render the animation: python hd-wallet.py
    
    import sys
    from manim.cli.render.commands import render
    
    # Set up rendering with medium quality and preview
    sys.argv = ["manim", "hd-wallet.py", "BitcoinWalletAnimation", "-pql"]
    render()
