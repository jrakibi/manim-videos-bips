from manim import *
import random
import hashlib
import math

# Sample BIP-39 mnemonic words (for Step 4 mapping)
BIP39_WORDS = [
    "abandon", "ability", "able", "about", "above", "absent", "absorb", "abstract",
    "absurd", "abuse", "access", "accident", "account", "accuse", "achieve", "acid",
    "acoustic", "acquire", "across", "act", "action", "actor", "actual", "adapt",
    "add", "addict", "address", "adjust", "admit", "adult", "advance", "advice",
    "aerobic", "affair", "afford", "afraid", "again", "age", "agent", "agree",
    "ahead", "aim", "air", "airport", "aisle", "alarm", "album", "alcohol", "alert",
    "alien", "all", "alley", "allow", "almost", "alone", "alpha", "already", "also",
    "alter", "always", "amateur", "amazing", "among", "amount", "amused", "analyst"
    # In a real implementation, all 2048 words would be included
]

class MnemonicGenerationAnimation(Scene):
    def construct(self):
        # Add overview scene first
        self.show_overview_animation()
        
        # Existing steps remain
        self.generate_entropy_animation()
        self.hash_entropy_animation()
        self.combine_entropy_and_checksum_animation()
        self.split_and_map_to_words_animation()
        self.show_entropy_word_relationship()

    def show_overview_animation(self):
        # Create the question text
        question = Text(
            "How are mnemonic phrases generated?",
            font_size=48,
            color=WHITE
        ).move_to(ORIGIN)
        
        # Animate the question appearing
        self.play(Write(question), run_time=1)
        self.wait(0.5)
        
        # Create the "Let's see step by step" text
        steps_text = Text(
            "Let's see step by step...",
            font_size=36,
            color=BLUE_A
        ).next_to(question, DOWN, buff=0.8)
        
        # Fade in the steps text while fading out the question
        self.play(
            FadeIn(steps_text, shift=UP * 0.3),
            question.animate.fade(0.7),
            run_time=0.8
        )
        self.wait(0.3)
        
        # Fade everything out before starting the steps
        self.play(
            FadeOut(question),
            FadeOut(steps_text),
            run_time=0.8
        )

    def generate_entropy_animation(self):
        # Step 1 title
        title = Text("Step 1: Create a random sequence (entropy) of 128 to 256 bits.", font_size=32, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)  # Faster title write
        self.wait(0.2)  # Reduced wait time
        
        # Create a container for the binary digits - EVEN SMALLER
        container = Rectangle(
            width=9, height=5,  # Further reduced from 10x5.5 to 9x5
            stroke_color=WHITE,
            stroke_width=2,
            fill_color=BLACK,
            fill_opacity=0.2
        )
        container.next_to(title, DOWN, buff=0.6)
        
        # Create initial binary display with all zeros
        binary_rows = []
        for i in range(5):  # 5 rows for 130 bits
            row = Text("0" * 26, font_size=24)  # Reduced font size from 28 to 24
            if i == 0:
                row.move_to(container.get_center() + UP * 1.2)  # Reduced offset from 1.4 to 1.2
            else:
                row.next_to(binary_rows[i-1], DOWN, buff=0.2)
            binary_rows.append(row)
        
        binary_group = VGroup(*binary_rows)
        binary_group.move_to(container.get_center())
        
        # Add "entropy = " label with adjusted font
        entropy_label = Text("entropy = ", font_size=24, color=BLUE_B)  # Reduced from 28 to 24
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
        
        # IMPROVED ENTROPY GENERATION ANIMATION - Better synchronization
        for transition in range(3):  # Reduced to 3 transitions for speed
            # Generate new random binary for all rows
            new_rows = []
            for i in range(5):
                # Create a new row with random bits
                new_text = ''.join(random.choice(["0", "1"]) for _ in range(26))
                new_row = Text(new_text, font_size=24)  # Reduced font size from 28 to 24
                
                if i == 0:
                    new_row.move_to(container.get_center() + UP * 1.2)  # Reduced offset from 1.4 to 1.2
                else:
                    new_row.next_to(new_rows[i-1], DOWN, buff=0.2)
                new_rows.append(new_row)
            
            new_group = VGroup(*new_rows)
            new_group.move_to(container.get_center())
            
            # IMPROVED SYNCHRONIZED ANIMATION between flashing and entropy change
            if transition == 0:
                # First transition - simple transform
                self.play(
                    TransformFromCopy(binary_group, new_group),
                    FadeOut(binary_group),
                    run_time=0.5
                )
            else:
                # Create a flash effect that better synchronizes with the entropy change
                flash = container.copy().set_fill(BLUE_A, opacity=0.3)
                
                # Combined animation: flash and transform at the same time
                self.play(
                    AnimationGroup(
                        FadeIn(flash, rate_func=there_and_back, run_time=0.5),
                        ReplacementTransform(binary_group, new_group, run_time=0.5)
                    )
                )
            
            # Update binary_group to the new state
            binary_group = new_group
            
            self.wait(0.1)  # Reduced wait time
        
        # Generate the final 128-bit entropy (trimming to exactly 130 bits)
        final_entropy = ""
        for _ in range(130):
            final_entropy += random.choice(["0", "1"])
        
        # Format the final entropy into 5 rows (first 4 rows with 26 bits, last row with 24 bits)
        final_rows = []
        for i in range(4):  # First 4 rows
            row_text = final_entropy[i*26:(i+1)*26]  # 26 bits per row
            row = Text(row_text, font_size=24, color=GREEN_B)  # Reduced font size from 28 to 24
            if i == 0:
                row.move_to(container.get_center() + UP * 1.2)  # Reduced offset from 1.4 to 1.2
            else:
                row.next_to(final_rows[i-1], DOWN, buff=0.2)
            final_rows.append(row)
        
        # Last row with remaining 24 bits
        last_row_text = final_entropy[104:130]  # Last 24 bits
        last_row = Text(last_row_text, font_size=24, color=GREEN_B)  # Reduced font size from 28 to 24
        last_row.next_to(final_rows[3], DOWN, buff=0.2)
        final_rows.append(last_row)
        
        final_group = VGroup(*final_rows)
        final_group.move_to(container.get_center())
        
        # Final entropy transition with improved synchronization
        highlight = container.copy().set_stroke(color=GREEN, width=6)
        
        # Combined animation: flash and final entropy appear together
        self.play(
            AnimationGroup(
                FadeOut(binary_group),
                FadeIn(final_group),
                FadeIn(highlight, rate_func=there_and_back)
            ),
            run_time=0.7  # Faster animation
        )
        
        # Add a label for the final entropy - smaller and positioned below but closer
        final_label = Text("Final Entropy Generated", font_size=28, color=GREEN)  # Reduced from 36 to 28
        final_label.next_to(container, DOWN, buff=0.3)  # Reduced buffer from 0.5 to 0.3 to move it closer
        
        self.play(
            Write(final_label),
            container.animate.set_stroke(color=GREEN_B, width=3),
            run_time=0.5  # Faster animation
        )
        self.wait(0.5)  # Reduced wait time
        
        # Store the final entropy for later use
        self.entropy = final_entropy[:130]  # Ensure exactly 130 bits
        self.entropy_display = VGroup(container, final_group, final_label, entropy_label)
        self.step1_title = title  # Store title separately for transition
        
        # Keep the entropy displayed but fade out the label
        self.play(
            FadeOut(final_label),
            run_time=0.5
        )

    def hash_entropy_animation(self):
        # Step 2 title
        title = Text("Step 2: Hash the Entropy", font_size=40, color=YELLOW)
        title.to_edge(UP, buff=0.5)
        
        # Smooth transition from Step 1 to Step 2 title
        self.play(
            ReplacementTransform(self.step1_title, title),
            run_time=0.6
        )
        self.wait(0.2)
        
        # Get entropy display components
        container, final_group, _, entropy_label = self.entropy_display
        
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
        
        # Create a moving entropy animation that flows from Step 1 to Step 2
        moving_entropy = final_group.copy()
        
        # Create a visual effect of entropy flowing into the hash function
        self.play(
            # Move the entropy down and shrink it toward the entropy_text position
            moving_entropy.animate.scale(0.5).move_to(entropy_text.get_center()),
            # Fade out the original entropy display
            FadeOut(container),
            FadeOut(final_group),
            FadeOut(entropy_label),
            run_time=0.8
        )
        
        # Now show the hash function appearing as the entropy flows in
        self.play(
            ReplacementTransform(moving_entropy, entropy_text),
            Write(hash_function),
            Write(closing_paren),
            Write(equals),
            run_time=0.8
        )
        
        # Create a brace to indicate "Message/file"
        message_brace = Brace(entropy_text, DOWN, color=BLUE_B)
        message_label = Text("Entropy", font_size=32, color=BLUE_B)
        message_label.next_to(message_brace, DOWN, buff=0.2)
        
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
        title = Text("Step 3: Combine Entropy with Checksum", font_size=40, color=YELLOW)
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
        title = Text("Step 4: Split the result into 11-bit Segments", font_size=36, color=YELLOW)
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
        combined_label = Text("Combined bits (Entropy + Checksum):", font_size=21, color=BLUE)
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

        # Store ALL elements that need to be faded out
        self.split_map_elements = VGroup(
            segment_group,      # Contains segment boxes, texts
            lookup_group,       # Contains lookup table and related elements
            title,             # Step 4 title
            new_label,         # "12 Mnemonic Words" text
            segment_label,     # Any other labels
            step5_title,       # "Step 5: Map Segments to BIP-39 Words" title
        )

        # Don't fade out at the end of this scene - let the next scene handle the transition

    def show_entropy_word_relationship(self):
        # Create the new title first but don't show it
        # new_title = Text("Entropy Size to Mnemonic Word Count", font_size=30, color=YELLOW)
        # new_title.to_edge(UP, buff=0.3)
        
        # Create transition text
        transition_text = Text(
            "Now let's see how entropy size affects\nthe number of words generated...",
            font_size=32,
            color=BLUE_A
        ).move_to(ORIGIN)
        
        # Fade out ALL previous scene elements while fading in transition text
        self.play(
            FadeOut(self.split_map_elements, shift=DOWN * 0.3),  # Added shift for better effect
            FadeIn(transition_text, shift=UP * 0.3),
            run_time=1
        )
        self.wait(0.5)
        
        # Fade out transition text and fade in new title
        self.play(
            FadeOut(transition_text),
            # Write(new_title),
            run_time=0.8
        )
        
        # Continue with existing entropy relationship animation...
        # Create binary grid visualization
        def create_bit_grid(bits, color):
            rows = math.ceil(bits / 32)  # 32 bits per row for consistent width
            cols = 32
            grid = VGroup()
            count = 0
            for i in range(rows):
                row = VGroup()
                for j in range(cols):
                    if count < bits:
                        bit = Square(
                            side_length=0.1,
                            fill_color=BLACK,
                            fill_opacity=0.5,
                            stroke_color=color,
                            stroke_width=1
                        )
                        row.add(bit)
                    count += 1
                row.arrange(RIGHT, buff=0.02)
                grid.add(row)
            grid.arrange(DOWN, buff=0.02)
            return grid

        # Create grids for all entropy sizes
        colors = {
            128: BLUE,
            160: GREEN,
            192: YELLOW,
            224: ORANGE,
            256: RED
        }

        # Start with 128-bit entropy visualization (larger size)
        initial_grid = create_bit_grid(128, colors[128])
        initial_grid.scale(1.5)
        initial_grid.move_to(ORIGIN)

        # Add initial labels for 128-bit entropy
        entropy_label = Text("Initial Entropy: 128 bits", font_size=36, color=colors[128])
        entropy_label.next_to(initial_grid, UP, buff=0.3)
        
        word_count = (128 + 128//32) // 11
        word_label = Text(f"→ {word_count} mnemonic words", font_size=36, color=colors[128])
        word_label.next_to(initial_grid, DOWN, buff=0.3)

        # Show initial 128-bit grid with animation
        self.play(
            FadeIn(initial_grid),
            Write(entropy_label),
            Write(word_label)
        )

        # Fill grid with animated effect
        animations = []
        for cell in initial_grid:
            for bit in cell:
                animations.append(bit.animate.set_fill(colors[128], opacity=0.3))
        
        # Play animations in batches
        batch_size = 32
        for i in range(0, len(animations), batch_size):
            batch = animations[i:i + batch_size]
            self.play(*batch, run_time=0.2)

        self.wait(0.5)

        # Now zoom out and show all entropy sizes
        grids = {}
        grid_group = VGroup()
        
        # Create all grids including 128 (new smaller version)
        for bits in [128, 160, 192, 224, 256]:
            grid = create_bit_grid(bits, colors[bits])
            grid.scale(0.8)
            grids[bits] = grid
            grid_group.add(grid)

        # Arrange all grids vertically
        grid_group.arrange(DOWN, buff=0.3)
        grid_group.move_to(ORIGIN)

        # Animate transition
        self.play(
            FadeOut(initial_grid),
            FadeIn(grids[128]),
            FadeOut(entropy_label),
            FadeOut(word_label),
            run_time=0.8
        )

        # Add labels and animate remaining grids one by one
        for bits in [128, 160, 192, 224, 256]:
            grid = grids[bits]
            
            bit_label = Text(f"Entropy: {bits} bits →", font_size=24, color=colors[bits])
            bit_label.next_to(grid, LEFT, buff=0.2)
            
            words = (bits + bits//32) // 11
            word_label = Text(f"→ {words} words", font_size=24, color=colors[bits])
            word_label.next_to(grid, RIGHT, buff=0.2)

            if bits > 128:
                self.play(
                    FadeIn(grid),
                    Write(bit_label),
                    Write(word_label),
                    run_time=0.6
                )

                # Fill grid with animated effect
                animations = []
                for cell in grid:
                    for bit in cell:
                        animations.append(bit.animate.set_fill(colors[bits], opacity=0.3))
                
                for i in range(0, len(animations), batch_size):
                    batch = animations[i:i + batch_size]
                    self.play(*batch, run_time=0.2)
            else:
                self.play(
                    Write(bit_label),
                    Write(word_label),
                    run_time=0.6
                )

        # Add security level indicators
        security_levels = [
            (128, "Standard Security"),
            (160, "Enhanced Security"),
            (192, "Strong Security"),
            (224, "Very Strong Security"),
            (256, "Maximum Security")
        ]

        for bits, level in security_levels:
            security_text = Text(level, font_size=20, color=colors[bits])
            security_text.next_to(grids[bits], RIGHT, buff=2.0)
            self.play(Write(security_text), run_time=0.4)

        self.wait(1)


if __name__ == "__main__":
    # This allows the script to be run directly
    import sys
    from manim.cli.render.commands import render
    
    # Set up rendering with medium quality and preview
    sys.argv = ["manim", "hd-wallet-scene55.py", "MnemonicGenerationAnimation", "-pql"]
    render()