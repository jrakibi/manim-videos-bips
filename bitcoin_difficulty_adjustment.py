from manim import *
import numpy as np

class BitcoinDifficultyAdjustment(Scene):
    def construct(self):
        # Title and introduction
        title = Text("Bitcoin Difficulty Adjustment", font_size=48)
        subtitle = Text("How Bitcoin maintains a 10-minute block time", font_size=32)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Explain the basics of mining and blocks
        mining_title = Text("Bitcoin Mining Basics", font_size=40)
        self.play(Write(mining_title))
        self.wait(1)
        self.play(mining_title.animate.to_edge(UP))
        
        # Create a visual representation of blocks
        blocks = VGroup(*[Rectangle(height=1, width=2, fill_opacity=0.7, fill_color=BLUE) 
                         for _ in range(6)])
        blocks.arrange(RIGHT, buff=0.3)
        blocks.next_to(mining_title, DOWN, buff=1)
        
        # Add timestamps to blocks
        timestamps = VGroup()
        base_time = 0
        times = []
        
        # First set of blocks with 10-minute intervals
        for i in range(6):
            base_time += 10
            times.append(base_time)
            time_text = Text(f"{base_time} min", font_size=20)
            time_text.next_to(blocks[i], DOWN)
            timestamps.add(time_text)
        
        # Animate blocks appearing with timestamps
        for i in range(6):
            self.play(
                FadeIn(blocks[i]),
                Write(timestamps[i]),
                run_time=0.5
            )
        
        # Explain target block time
        target_text = Text("Target: One block every 10 minutes", color=GREEN, font_size=30)
        target_text.next_to(blocks, DOWN, buff=1)
        self.play(Write(target_text))
        self.wait(2)
        
        # Clear the scene for the next explanation
        self.play(
            FadeOut(blocks),
            FadeOut(timestamps),
            FadeOut(target_text),
            FadeOut(mining_title)
        )
        
        # Explain difficulty adjustment
        adjustment_title = Text("Difficulty Adjustment", font_size=40)
        self.play(Write(adjustment_title))
        self.wait(1)
        self.play(adjustment_title.animate.to_edge(UP))
        
        # Create a visual representation of the difficulty adjustment period
        period_text = Text("Every 2016 blocks (≈2 weeks), Bitcoin adjusts mining difficulty", font_size=30)
        period_text.next_to(adjustment_title, DOWN, buff=0.5)
        self.play(Write(period_text))
        self.wait(2)
        
        # Create a formula for difficulty adjustment
        formula = MathTex(r"\text{New Difficulty} = \text{Old Difficulty} \times \frac{\text{Actual Time}}{\text{Expected Time}}")
        formula.next_to(period_text, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(2)
        
        # Expected time explanation
        expected_time = Text("Expected Time = 2016 blocks × 10 minutes = 20,160 minutes (2 weeks)", font_size=25)
        expected_time.next_to(formula, DOWN, buff=0.5)
        self.play(Write(expected_time))
        self.wait(2)
        
        # Clear for scenario demonstrations
        self.play(
            FadeOut(formula),
            FadeOut(expected_time),
            FadeOut(period_text)
        )
        
        # Scenario 1: Blocks are being mined too quickly
        scenario1 = Text("Scenario 1: Blocks are mined too quickly", font_size=35, color=RED)
        scenario1.next_to(adjustment_title, DOWN, buff=0.5)
        self.play(Write(scenario1))
        
        # Create fast blocks
        fast_blocks = VGroup(*[Rectangle(height=1, width=2, fill_opacity=0.7, fill_color=RED) 
                             for _ in range(6)])
        fast_blocks.arrange(RIGHT, buff=0.3)
        fast_blocks.next_to(scenario1, DOWN, buff=1)
        
        # Add timestamps to fast blocks
        fast_timestamps = VGroup()
        base_time = 0
        
        # Blocks with 5-minute intervals (too fast)
        for i in range(6):
            base_time += 5
            time_text = Text(f"{base_time} min", font_size=20)
            time_text.next_to(fast_blocks[i], DOWN)
            fast_timestamps.add(time_text)
        
        # Animate fast blocks appearing with timestamps
        for i in range(6):
            self.play(
                FadeIn(fast_blocks[i]),
                Write(fast_timestamps[i]),
                run_time=0.4
            )
        
        # Show the adjustment calculation
        fast_calc = MathTex(
            r"\text{New Difficulty} &= \text{Old Difficulty} \times \frac{\text{Actual Time}}{\text{Expected Time}}\\",
            r"&= \text{Old Difficulty} \times \frac{10,080 \text{ min}}{20,160 \text{ min}}\\",
            r"&= \text{Old Difficulty} \times 0.5"
        )
        fast_calc.scale(0.4)  # Make it smaller to fit on screen
        fast_calc.next_to(fast_blocks, DOWN, buff=1)
        self.play(Write(fast_calc))
        
        # Show the result
        fast_result = Text("Result: Difficulty INCREASES to slow down block production", font_size=26, color=RED)
        fast_result.scale(0.9)  # Make it smaller
        fast_result.next_to(fast_calc, DOWN, buff=0.5)
        self.play(Write(fast_result))
        self.wait(2)
        
        # Clear for next scenario
        self.play(
            FadeOut(fast_blocks),
            FadeOut(fast_timestamps),
            FadeOut(fast_calc),
            FadeOut(fast_result),
            FadeOut(scenario1)
        )
        
        # Scenario 2: Blocks are being mined too slowly
        scenario2 = Text("Scenario 2: Blocks are mined too slowly", font_size=35, color=BLUE)
        scenario2.next_to(adjustment_title, DOWN, buff=0.5)
        self.play(Write(scenario2))
        
        # Create slow blocks
        slow_blocks = VGroup(*[Rectangle(height=1, width=2, fill_opacity=0.7, fill_color=BLUE) 
                             for _ in range(6)])
        slow_blocks.arrange(RIGHT, buff=0.3)
        slow_blocks.next_to(scenario2, DOWN, buff=1)
        
        # Add timestamps to slow blocks
        slow_timestamps = VGroup()
        base_time = 0
        
        # Blocks with 15-minute intervals (too slow)
        for i in range(6):
            base_time += 15
            time_text = Text(f"{base_time} min", font_size=20)
            time_text.next_to(slow_blocks[i], DOWN)
            slow_timestamps.add(time_text)
        
        # Animate slow blocks appearing with timestamps
        for i in range(6):
            self.play(
                FadeIn(slow_blocks[i]),
                Write(slow_timestamps[i]),
                run_time=0.6
            )
        
        # Show the adjustment calculation
        slow_calc = MathTex(
            r"\text{New Difficulty} &= \text{Old Difficulty} \times \frac{\text{Actual Time}}{\text{Expected Time}}\\",
            r"&= \text{Old Difficulty} \times \frac{30,240 \text{ min}}{20,160 \text{ min}}\\",
            r"&= \text{Old Difficulty} \times 1.5"
        )
        slow_calc.scale(0.4)  # Make it smaller to fit on screen
        slow_calc.next_to(slow_blocks, DOWN, buff=1)
        self.play(Write(slow_calc))
        
        # Show the result
        slow_result = Text("Result: Difficulty DECREASES to speed up block production", font_size=26, color=BLUE)
        slow_result.scale(0.9)  # Make it smaller
        slow_result.next_to(slow_calc, DOWN, buff=0.5)
        self.play(Write(slow_result))
        self.wait(2)
        
        # Clear for final explanation
        self.play(
            FadeOut(slow_blocks),
            FadeOut(slow_timestamps),
            FadeOut(slow_calc),
            FadeOut(slow_result),
            FadeOut(scenario2),
            FadeOut(adjustment_title)
        )
        
        # Final explanation with hashrate visualization
        final_title = Text("How Difficulty Works with Hashrate", font_size=40)
        self.play(Write(final_title))
        self.wait(1)
        self.play(final_title.animate.to_edge(UP))
        
        # Create a visualization of the target hash
        target_explanation = Text("Bitcoin miners must find a hash below the target value", font_size=30)
        target_explanation.next_to(final_title, DOWN, buff=0.5)
        self.play(Write(target_explanation))
        
        # Create a number line representing the hash space
        hash_space = NumberLine(
            x_range=[0, 1, 0.1],
            length=10,
            include_numbers=True,
            include_tip=True,
        )
        hash_space.next_to(target_explanation, DOWN, buff=1)
        self.play(Create(hash_space))
        
        # Show the target on the number line
        target_value = 0.3
        target_point = hash_space.number_to_point(target_value)
        target_dot = Dot(target_point, color=GREEN)
        target_label = Text("Target", font_size=20, color=GREEN)
        target_label.next_to(target_dot, UP)
        
        target_area = Rectangle(
            width=hash_space.number_to_point(target_value)[0] - hash_space.number_to_point(0)[0],
            height=0.5,
            fill_color=GREEN,
            fill_opacity=0.5
        )
        target_area.next_to(hash_space, UP, buff=0)
        target_area.align_to(hash_space, LEFT)
        
        self.play(
            Create(target_dot),
            Write(target_label),
            Create(target_area)
        )
        
        # Explain that lower target = higher difficulty
        difficulty_text = Text("Lower target = Higher difficulty = Fewer valid hashes", font_size=25)
        difficulty_text.next_to(hash_space, DOWN, buff=0.5)
        self.play(Write(difficulty_text))
        self.wait(2)
        
        # Show difficulty adjustment
        # First, make the target smaller (higher difficulty)
        new_target_value = 0.1
        new_target_point = hash_space.number_to_point(new_target_value)
        new_target_dot = Dot(new_target_point, color=RED)
        new_target_label = Text("New Target\n(Higher Difficulty)", font_size=20, color=RED)
        new_target_label.next_to(new_target_dot, UP)
        
        new_target_area = Rectangle(
            width=hash_space.number_to_point(new_target_value)[0] - hash_space.number_to_point(0)[0],
            height=0.5,
            fill_color=RED,
            fill_opacity=0.5
        )
        new_target_area.next_to(hash_space, UP, buff=0)
        new_target_area.align_to(hash_space, LEFT)
        
        self.play(
            Transform(target_area, new_target_area),
            Transform(target_dot, new_target_dot),
            Transform(target_label, new_target_label)
        )
        
        higher_diff_text = Text("When blocks are found too quickly, target decreases (difficulty increases)", 
                               font_size=25, color=RED)
        higher_diff_text.next_to(difficulty_text, DOWN, buff=0.5)
        self.play(Write(higher_diff_text))
        self.wait(2)
        
        # Then, make the target larger (lower difficulty)
        newer_target_value = 0.5
        newer_target_point = hash_space.number_to_point(newer_target_value)
        newer_target_dot = Dot(newer_target_point, color=BLUE)
        newer_target_label = Text("New Target\n(Lower Difficulty)", font_size=20, color=BLUE)
        newer_target_label.next_to(newer_target_dot, UP)
        
        newer_target_area = Rectangle(
            width=hash_space.number_to_point(newer_target_value)[0] - hash_space.number_to_point(0)[0],
            height=0.5,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        newer_target_area.next_to(hash_space, UP, buff=0)
        newer_target_area.align_to(hash_space, LEFT)
        
        self.play(
            Transform(target_area, newer_target_area),
            Transform(target_dot, newer_target_dot),
            Transform(target_label, newer_target_label)
        )
        
        lower_diff_text = Text("When blocks are found too slowly, target increases (difficulty decreases)", 
                              font_size=25, color=BLUE)
        lower_diff_text.next_to(higher_diff_text, DOWN, buff=0.5)
        self.play(Write(lower_diff_text))
        self.wait(2)
        
        # Final summary
        self.play(
            FadeOut(target_area),
            FadeOut(target_dot),
            FadeOut(target_label),
            FadeOut(hash_space),
            FadeOut(target_explanation),
            FadeOut(difficulty_text),
            FadeOut(higher_diff_text),
            FadeOut(lower_diff_text),
            FadeOut(final_title)
        )
        
        summary_title = Text("Bitcoin Difficulty Adjustment: Summary", font_size=40)
        self.play(Write(summary_title))
        self.wait(1)
        self.play(summary_title.animate.to_edge(UP))
        
        summary_points = VGroup(
            Text("• Bitcoin aims for one block every 10 minutes", font_size=30),
            Text("• Difficulty adjusts every 2016 blocks (≈2 weeks)", font_size=30),
            Text("• If blocks are too fast → Difficulty increases", font_size=30),
            Text("• If blocks are too slow → Difficulty decreases", font_size=30),
            Text("• This maintains Bitcoin's predictable issuance schedule", font_size=30)
        )
        summary_points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        summary_points.next_to(summary_title, DOWN, buff=1)
        
        for point in summary_points:
            self.play(Write(point), run_time=0.8)
        
        self.wait(3)
        
        # Final message
        final_message = Text("Bitcoin's difficulty adjustment is a key mechanism\nthat ensures network stability and security", 
                            font_size=35, color=YELLOW)
        final_message.next_to(summary_points, DOWN, buff=1)
        self.play(Write(final_message))
        self.wait(3)
        
        # Fade everything out
        self.play(
            FadeOut(summary_title),
            FadeOut(summary_points),
            FadeOut(final_message)
        )
        
        # Add an improved mining simulation section
        mining_sim_title = Text("Mining Simulation: Finding Valid Blocks", font_size=40)
        self.play(Write(mining_sim_title))
        self.wait(1)
        self.play(mining_sim_title.animate.to_edge(UP))
        
        # Create a visual representation of hash attempts
        hash_attempts_text = Text("Hash attempts by miners", font_size=30)
        hash_attempts_text.next_to(mining_sim_title, DOWN, buff=0.8)
        self.play(Write(hash_attempts_text))
        
        # Create a grid of hash attempts - smaller and more compact
        hash_grid = VGroup()
        rows, cols = 4, 8
        for i in range(rows):
            for j in range(cols):
                square = Square(side_length=0.5, fill_opacity=0.5, fill_color=GRAY)
                square.move_to([j*0.6 - 2.1, -i*0.6 + 1, 0])
                hash_grid.add(square)
        
        self.play(Create(hash_grid))
        
        # Normal difficulty - show valid hashes
        normal_diff_text = Text("Normal Difficulty", font_size=28, color=YELLOW)
        normal_diff_text.to_edge(LEFT).shift(RIGHT * 2 + UP * 0.5)
        self.play(Write(normal_diff_text))
        
        # Highlight valid hashes (below target) in green
        valid_indices = [3, 11, 17, 25]  # Random indices for valid hashes
        for idx in valid_indices:
            self.play(
                hash_grid[idx].animate.set_fill(GREEN, opacity=0.8),
                run_time=0.4
            )
        
        # Add a simple explanation
        valid_text = Text("4 valid blocks found", font_size=24, color=GREEN)
        valid_text.next_to(hash_grid, DOWN, buff=0.5)
        self.play(Write(valid_text))
        
        # Add time indicator
        time_text = Text("Time to mine 2016 blocks: 2 weeks (target)", font_size=24)
        time_text.next_to(valid_text, DOWN, buff=0.5)
        self.play(Write(time_text))
        self.wait(2)
        
        # Clear for high difficulty
        self.play(
            FadeOut(normal_diff_text),
            FadeOut(valid_text),
            FadeOut(time_text),
            *[square.animate.set_fill(GRAY, opacity=0.5) for square in hash_grid]
        )
        
        # High difficulty scenario
        high_diff_text = Text("Higher Difficulty", font_size=28, color=RED)
        high_diff_text.to_edge(LEFT).shift(RIGHT * 2 + UP * 0.5)
        self.play(Write(high_diff_text))
        
        # With higher difficulty, only 2 valid hashes
        harder_valid_indices = [7, 22]
        for idx in harder_valid_indices:
            self.play(
                hash_grid[idx].animate.set_fill(GREEN, opacity=0.8),
                run_time=0.4
            )
        
        # Add explanation for high difficulty
        harder_valid_text = Text("Only 2 valid blocks found", font_size=24, color=RED)
        harder_valid_text.next_to(hash_grid, DOWN, buff=0.5)
        self.play(Write(harder_valid_text))
        
        # Add time indicator for high difficulty
        harder_time_text = Text("Time to mine 2016 blocks: 4 weeks (too slow)", font_size=24)
        harder_time_text.next_to(harder_valid_text, DOWN, buff=0.5)
        self.play(Write(harder_time_text))
        
        # Add adjustment explanation
        adjustment_text = Text("Result: Difficulty will DECREASE", font_size=28, color=BLUE)
        adjustment_text.next_to(harder_time_text, DOWN, buff=0.5)
        self.play(Write(adjustment_text))
        self.wait(2)
        
        # Clear for low difficulty
        self.play(
            FadeOut(high_diff_text),
            FadeOut(harder_valid_text),
            FadeOut(harder_time_text),
            FadeOut(adjustment_text),
            *[square.animate.set_fill(GRAY, opacity=0.5) for square in hash_grid]
        )
        
        # Low difficulty scenario
        low_diff_text = Text("Lower Difficulty", font_size=28, color=BLUE)
        low_diff_text.to_edge(LEFT).shift(RIGHT * 2 + UP * 0.5)
        self.play(Write(low_diff_text))
        
        # With lower difficulty, more valid hashes
        easier_valid_indices = [1, 5, 9, 13, 18, 22, 26, 30]
        for idx in easier_valid_indices:
            self.play(
                hash_grid[idx].animate.set_fill(GREEN, opacity=0.8),
                run_time=0.3
            )
        
        # Add explanation for low difficulty
        easier_valid_text = Text("8 valid blocks found (too many)", font_size=24, color=BLUE)
        easier_valid_text.next_to(hash_grid, DOWN, buff=0.5)
        self.play(Write(easier_valid_text))
        
        # Add time indicator for low difficulty
        easier_time_text = Text("Time to mine 2016 blocks: 1 week (too fast)", font_size=24)
        easier_time_text.next_to(easier_valid_text, DOWN, buff=0.5)
        self.play(Write(easier_time_text))
        
        # Add adjustment explanation
        easier_adjustment_text = Text("Result: Difficulty will INCREASE", font_size=28, color=RED)
        easier_adjustment_text.next_to(easier_time_text, DOWN, buff=0.5)
        self.play(Write(easier_adjustment_text))
        self.wait(2)
        
        # Final explanation about the balance
        self.play(
            FadeOut(low_diff_text),
            FadeOut(easier_valid_text),
            FadeOut(easier_time_text),
            FadeOut(easier_adjustment_text),
            *[square.animate.set_fill(GRAY, opacity=0.5) for square in hash_grid]
        )
        
        balance_title = Text("Difficulty Balancing Act", font_size=30, color=YELLOW)
        balance_title.next_to(hash_attempts_text, DOWN, buff=1.5)
        self.play(Write(balance_title))
        
        balance_text = Text("Bitcoin automatically adjusts difficulty to maintain\n10-minute average block time", 
                           font_size=26)
        balance_text.next_to(balance_title, DOWN, buff=0.5)
        self.play(Write(balance_text))
        self.wait(2)
        
        # Clear the mining simulation
        self.play(
            FadeOut(mining_sim_title),
            FadeOut(hash_attempts_text),
            FadeOut(hash_grid),
            FadeOut(balance_title),
            FadeOut(balance_text)
        )
        
        # Final conclusion - simplified
        final_title = Text("Bitcoin's Difficulty Adjustment", font_size=48, color=YELLOW)
        self.play(Write(final_title))
        self.wait(1)
        self.play(final_title.animate.to_edge(UP))
        
        final_points = VGroup(
            Text("• Maintains 10-minute block time", font_size=30),
            Text("• Adjusts every 2016 blocks", font_size=30),
            Text("• Responds to changes in network hashrate", font_size=30),
            Text("• Ensures predictable Bitcoin issuance", font_size=30)
        )
        final_points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(final_title, DOWN, buff=1)
        
        for point in final_points:
            self.play(Write(point), run_time=0.8)
        
        self.wait(3)
        
        # Final fade out
        self.play(
            FadeOut(final_title),
            FadeOut(final_points)
        ) 