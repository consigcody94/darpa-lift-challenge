# DARPA Lift Challenge - Design Decision Matrix

## Quick Comparison: Top 3 Design Approaches

### Scoring Criteria (1-10 scale, 10 = best)

| Criteria | Weight | Quadplane Hybrid VTOL | Optimized Octocopter | Tiltrotor |
|----------|--------|----------------------|----------------------|-----------|
| **Payload Ratio Potential** | 25% | 8 (4.9:1) | 9 (5.9:1) | 7 (4.2:1) |
| **Energy Efficiency** | 20% | 10 | 5 | 9 |
| **Technical Feasibility** | 20% | 7 | 9 | 6 |
| **Development Complexity** | 15% | 5 | 9 | 4 |
| **Reliability** | 10% | 7 | 8 | 6 |
| **Wind Tolerance** | 5% | 8 | 6 | 7 |
| **Control Stability** | 5% | 6 | 9 | 5 |
| **TOTAL WEIGHTED SCORE** | | **7.65** | **7.70** | **6.55** |

### Winner: **Tie between Quadplane and Octocopter** (Slight edge to Octocopter on feasibility)

---

## Detailed Analysis

### Option 1: Quadplane Hybrid VTOL ⭐ PRIMARY RECOMMENDATION

**Configuration:** Fixed wing + 4 vertical lift motors + pusher prop + hybrid power

**Strengths:**
- Best cruise efficiency (30-40% better than multirotor)
- Competitive payload ratio (4.9:1)
- Eligible for "Revolutionary Aerodynamic Design" bonus prize
- Proven technology (ArduPilot QuadPlane)
- Good wind tolerance in cruise

**Weaknesses:**
- Complex transition flight phase
- More development/tuning time needed
- Wing adds some weight
- Requires extensive flight testing

**Critical Path Items:**
1. Hybrid power system procurement (12-week lead time)
2. Wing design and optimization (CFD + testing)
3. Transition flight tuning (high risk area)
4. Payload CG management

**Risk Level:** Medium-High
**Development Time:** 9-10 months
**Estimated Cost:** $40,000-50,000

**Recommendation:** Choose this if:
- You have strong aerodynamics/controls expertise
- You have 9+ months development time
- You want to compete for bonus design prizes
- You prioritize efficiency and innovation

---

### Option 2: Optimized Octocopter ⭐ ALTERNATIVE RECOMMENDATION

**Configuration:** Coaxial octocopter + large props + hybrid power + minimal frame

**Strengths:**
- **Highest theoretical payload ratio (5.9:1)**
- Simplest design (no transitions)
- Fastest development time
- Most reliable/robust
- Excellent hover stability
- Proven multirotor control

**Weaknesses:**
- High power consumption throughout mission
- Less efficient cruise
- Larger, more powerful hybrid generator needed (heavier)
- Time margin tighter (higher risk)
- Not eligible for aerodynamic design prize

**Critical Path Items:**
1. Hybrid power system (need 5-6 kW continuous)
2. Ultra-lightweight frame design
3. Large propeller selection/optimization
4. Energy management for 30-min mission

**Risk Level:** Medium
**Development Time:** 6-7 months
**Estimated Cost:** $35,000-45,000

**Recommendation:** Choose this if:
- Development timeline is shorter (<8 months)
- Team has limited VTOL transition experience
- Prioritizing reliability over efficiency
- Want highest payload ratio potential
- Prefer simpler, proven technology

---

### Option 3: Tiltrotor

**Configuration:** 4 tilting motors + wing + hybrid power

**Strengths:**
- Good cruise efficiency
- Compact design
- No extra cruise motor needed

**Weaknesses:**
- Most complex transition mechanism
- Tilting mechanism adds significant weight
- Unproven at this scale for heavy lift
- Highest development risk
- Complex control algorithms

**Risk Level:** High
**Development Time:** 12+ months
**Estimated Cost:** $50,000-60,000

**Recommendation:** ❌ Not recommended for this competition
- Too high risk for timeline
- Weight penalty from tilt mechanisms
- No clear advantage over quadplane
- Better suited for long-range missions (not this 5nm profile)

---

## Head-to-Head: Quadplane vs Octocopter

### Power Budget Comparison

| Phase | Quadplane Power | Octocopter Power | Advantage |
|-------|----------------|------------------|-----------|
| Hover/Takeoff | 8,000 W | 8,500 W | Quadplane (-6%) |
| Loaded Cruise | 5,000 W | 7,000 W | Quadplane (-29%) |
| Unloaded Cruise | 3,000 W | 4,500 W | Quadplane (-33%) |
| **Total Energy** | **2,109 Wh** | **2,920 Wh** | **Quadplane (-28%)** |

### Weight Budget Comparison

| Component | Quadplane | Octocopter | Difference |
|-----------|-----------|------------|------------|
| Frame/Structure | 5.0 kg | 2.0 kg | Octo -3.0 kg |
| Wing | 3.5 kg | 0 kg | Octo -3.5 kg |
| Motors + Controllers | 3.5 kg | 4.0 kg | Quadplane -0.5 kg |
| Hybrid Power System | 6.5 kg | 7.5 kg | Quadplane -1.0 kg |
| Landing Gear | 1.0 kg | 1.0 kg | Tie |
| Electronics | 0.8 kg | 0.8 kg | Tie |
| Payload Mount | 0.5 kg | 0.5 kg | Tie |
| **TOTAL** | **20.8 kg (45.9 lb)** | **15.8 kg (34.8 lb)** | **Octo -5.0 kg** |

### Payload Capacity Comparison

**Quadplane:**
- Aircraft: 45.9 lbs
- Margin to 55 lb: 9.1 lbs
- Target payload: 220 lbs
- **Ratio: 4.79:1**

**Octocopter:**
- Aircraft: 34.8 lbs
- Margin to 55 lb: 20.2 lbs
- Target payload: 240 lbs
- **Ratio: 6.90:1**

**Winner:** Octocopter by significant margin

### Energy Margin Comparison

**Quadplane:**
- Required: 2,109 Wh
- Hybrid can provide: 3,500+ Wh
- **Margin: 66%** ✅ Comfortable

**Octocopter:**
- Required: 2,920 Wh
- Hybrid can provide: 4,000+ Wh (with larger generator)
- **Margin: 37%** ⚠️ Acceptable but tight

---

## FINAL RECOMMENDATION

### Primary Choice: **Optimized Octocopter with Hybrid Power**

**Rationale:**

1. **Highest Winning Potential:** 6.9:1 ratio vs 4.8:1 for quadplane
   - This is 73% higher ratio than competition goal (4:1)
   - Likely to be top-tier performance

2. **Lower Risk:** Simpler design = fewer failure modes
   - No transition phase to fail
   - Proven multirotor control
   - Faster development timeline

3. **Better Weight Budget:** 11 lbs lighter aircraft
   - More margin for iteration
   - Can afford some weight growth
   - Allows heavier/more robust components

4. **Faster Time to Market:**
   - 6-7 months vs 9-10 months
   - More time for testing and optimization
   - Can start later if needed

5. **Still Innovative:** Eligible for "Revolutionary Powertrain" prize
   - Hybrid system at this scale is novel
   - Ultra-lightweight frame design
   - Low disk loading optimization

**The Trade-off:**
- Less energy efficient (needs more powerful hybrid)
- Tighter time margin (but still 5+ min buffer)
- Not eligible for aerodynamic design prize

**Why It's Worth It:**
- **The scoring metric is payload/aircraft ratio, not efficiency**
- Octocopter is 44% better on the actual scoring metric
- Lower technical risk for similar cost
- Better chance of completing mission successfully

### Backup Choice: **Quadplane Hybrid VTOL**

**Use if:**
- Team has strong aerodynamics background
- Development starts immediately (need full 10 months)
- Want to compete for multiple prize categories
- Priority on innovation over raw performance

**Timeline Decision Point:**
- If starting before February 2026: Either design viable
- If starting after February 2026: Octocopter only

---

## Implementation Strategy

### Recommended Approach: **Dual-Track Development**

**Phase 1 (Months 1-2): Parallel Investigation**
- Build small-scale test octocopter (1/4 scale)
- Simultaneously do detailed quadplane simulation
- Procure hybrid power system (works for both)
- Build test stand for power system validation

**Phase 2 (Month 3): Down-Select**
- Based on test results, commit to one design
- If octocopter tests show good control → Go with octocopter
- If timeline allows and team confident → Go with quadplane
- Point of no return: End of Month 3

**Phase 3 (Months 4-10): Full Development**
- Follow committed design path
- See detailed roadmap in main analysis document

**Budget for Dual-Track:**
- Small octocopter test: $2,000
- Quadplane simulation/analysis: $1,000
- Shared hybrid power system: $4,000
- **Total additional: $3,000** (vs single-track)
- **Benefit:** De-risk design choice, validate assumptions

---

## Success Probability Estimates

### Octocopter
- Complete mission successfully: **80%**
- Achieve 5:1+ ratio: **70%**
- Place in top 3: **40%**
- Win 1st place: **15%**

### Quadplane
- Complete mission successfully: **65%**
- Achieve 4.5:1+ ratio: **60%**
- Place in top 3: **35%**
- Win 1st place: **12%**
- Win secondary prize: **25%**

**Highest Expected Value: Octocopter**

---

## Go/No-Go Decision Criteria

### Green Light Requirements (Must have ALL):
✅ Team with aerospace/controls/structures expertise
✅ Budget of $40,000-60,000
✅ Development timeline of 6+ months
✅ Access to flight testing facility
✅ Hybrid power system availability confirmed

### Red Flags (ANY of these = Reconsider):
❌ Less than 5 months to competition
❌ No prior VTOL/drone development experience
❌ Budget under $30,000
❌ Cannot source hybrid power system
❌ No safe flight testing location

### Decision: **GO** if green lights met, **NO-GO** if any red flags

---

**Last Updated:** November 22, 2025
**Decision Required By:** December 15, 2025 (to meet development timeline)
**Registration Opens:** January 5, 2026
**Competition Date:** Summer 2026
