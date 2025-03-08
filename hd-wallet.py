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
        self.scene4_deterministic_wallets()
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
