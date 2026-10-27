comparison = anova_lm(res_two, res_quad)
print(comparison.to_string())

F_manual = ((res_two.ssr - res_quad.ssr) /
            (res_two.df_resid - res_quad.df_resid)) / (
                res_quad.ssr / res_quad.df_resid)
print('F by hand:', F_manual)
